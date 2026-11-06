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

def test_timestamp_helper_is_used(monkeypatch):
    from app.services import audit_service
    monkeypatch.setattr(audit_service,"iso_timestamp",lambda event:"CONTROL")
    assert api.create().timestamp_text(None)=="CONTROL"
