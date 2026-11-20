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

def test_legacy_format():
    from app.domain.audit import AuditEvent
    from app.domain.adapters import LegacyAuditAdapter
    class Legacy:
        def to_text(self,item):return item["event_id"]
    item=AuditEvent("E","CARD_BLOCKED","C",datetime(2030,5,1,tzinfo=timezone.utc),{})
    assert LegacyAuditAdapter(Legacy()).format(item)=="E"
