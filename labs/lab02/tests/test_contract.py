import pytest
from decimal import Decimal
from datetime import date, datetime, timezone, timedelta
from app import api
from app.support.errors import DomainError
from app.support.types import Repository, CheckResult, Money, money


def error(code, operation):
    with pytest.raises(DomainError) as caught:
        operation()
    assert caught.value.code == code


def invoke(service, method, *args, **kwargs):
    return api.call(service, method, *args, **kwargs)

STAMP=datetime(2030,5,1,12,tzinfo=timezone.utc)

def event(key="E1",entity_id="TX-1",kind="PAYMENT_APPROVED",details=None):
    return api.make(key,kind,entity_id,STAMP,{} if details is None else details)

def test_record_find_order_and_supplied_time():
    service=api.create()
    first,second=event(),event("E2","TX-2")
    invoke(service,"record",first)
    invoke(service,"record",second)
    assert invoke(service,"find")== (first,second)
    assert invoke(service,"find",entity_id="TX-1")== (first,)
    assert api.view(first)["timestamp"]==STAMP
    assert invoke(service,"render",entity_id="TX-1")== ("E1|PAYMENT_APPROVED|TX-1",)

def test_independent_empty_repository():
    invoke(api.create(),"record",event())
    assert invoke(api.create(),"find")==()

def test_input_and_output_details_are_snapshots():
    details={"reason":"X"}
    item=event(details=details)
    details["reason"]="Y"
    assert item.details=={"reason":"X"}
    item.details["reason"]="Z"
    assert item.details=={"reason":"X"}
    with pytest.raises(AttributeError):item.event_type="CARD_BLOCKED"

@pytest.mark.parametrize("stamp",[datetime(2030,5,1),datetime(2030,5,1,tzinfo=timezone(timedelta(hours=1))),STAMP.replace(microsecond=1)])
def test_invalid_timestamp(stamp):
    error("INVALID_TIMESTAMP",lambda:api.make("E","CARD_BLOCKED","C",stamp,{}))

def test_duplicate_id_does_not_replace_event():
    service=api.create()
    item=event()
    invoke(service,"record",item)
    error("DUPLICATE_EVENT",lambda:invoke(service,"record",event(details={"changed":"yes"})))
    assert invoke(service,"find")== (item,)
