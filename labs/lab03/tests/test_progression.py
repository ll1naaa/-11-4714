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
