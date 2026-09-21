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

def test_description():
    from app.domain.audit import AuditEvent
    item=AuditEvent("E1","PAYMENT_APPROVED","TX-1",datetime(2030,5,1,tzinfo=timezone.utc),{})
    assert item.describe()=="E1:PAYMENT_APPROVED:TX-1"
