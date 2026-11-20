import pytest
from datetime import date, datetime, timezone
from decimal import Decimal
from app import api
from app.support.errors import DomainError


def code(expected, operation):
    with pytest.raises(DomainError) as caught:
        operation()
    assert caught.value.code == expected

from app.domain.audit import AuditEvent

def test_progression_audit_snapshot_duplicate_then_success():
    service = api.create()
    stamp = datetime(2030, 5, 1, tzinfo=timezone.utc)
    details = {"reason": "FIRST"}
    first = AuditEvent("E1", "CARD_BLOCKED", "C", stamp, details)
    service.record(first)
    old = service.render()
    code("DUPLICATE_EVENT", lambda: service.record(first))
    details["reason"] = "CHANGED"
    service.record(AuditEvent("E2", "CARD_BLOCKED", "C", stamp, {"reason": "THIRD"}))
    assert len(service.render()) == 2 and service.render()[0] == old[0]
    assert first.details == {"reason": "FIRST"}

from app.domain.formatters import AuditFormatter

def test_progression_false_formatter_error_does_not_delete_event():
    calls = []
    class Once(AuditFormatter):
        def __bool__(self): return False
        def format(self, event):
            calls.append(event)
            if len(calls) == 1: raise DomainError("TEMPORARY")
            return "CONTROL:" + event.event_id
    service = api.create(formatter=Once())
    event = AuditEvent("E", "CARD_BLOCKED", "C", datetime(2030,5,1,tzinfo=timezone.utc), {})
    service.record(event)
    code("TEMPORARY", service.render)
    assert len(calls) == 1 and service.find() == (event,)
    assert service.render() == ("CONTROL:E",) and calls == [event, event]

from app.domain.audit import AuditEvent

def test_progression_extra_lab05():
    service = api.create()
    old = AuditEvent("E1", "PAYMENT_APPROVED", "T1", datetime(2030, 1, 1, tzinfo=timezone.utc), {"a": "1"})
    new = AuditEvent("E2", "PAYMENT_DECLINED", "T1", datetime(2030, 1, 2, tzinfo=timezone.utc), {"a": "2"})
    service.record(old)
    service.record(new)
    assert service.event_counts("T1") == {"PAYMENT_APPROVED": 1, "PAYMENT_DECLINED": 1}
    assert service.latest_event("T1") == new
    assert service.latest_event("UNKNOWN") is None
