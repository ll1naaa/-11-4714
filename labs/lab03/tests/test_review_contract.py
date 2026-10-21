import pytest
from decimal import Decimal
from datetime import date, datetime, timezone, timedelta
from app import api
from app.support.errors import DomainError


def assert_code(code, action):
    with pytest.raises(DomainError) as caught:
        action()
    assert caught.value.code == code

from app.support.types import money

@pytest.mark.parametrize("details",[{"nested":{"x":"y"}}, {"count":1}, {1:"x"}])
def test_review_details_are_flat_strings(details):
    assert_code("INVALID_DETAILS",lambda:api.make("E","CARD_BLOCKED","C",datetime(2030,5,1,tzinfo=timezone.utc),details))

def test_review_json_contains_all_event_fields():
    import json
    from app.domain.formatters import JsonAuditFormatter
    stamp=datetime(2030,5,1,tzinfo=timezone.utc)
    item=api.make("E","CARD_BLOCKED","C",stamp,{"reason":"Блокировка"})
    assert json.loads(JsonAuditFormatter().format(item)) == dict(event_id="E",event_type="CARD_BLOCKED",entity_id="C",timestamp=stamp.isoformat(),details={"reason":"Блокировка"})

def test_review_service_uses_formatter_in_lab3(monkeypatch):
    from app.domain.formatters import TextAuditFormatter
    calls=[]
    def format(self,event):calls.append(event);return "CONTROL"
    monkeypatch.setattr(TextAuditFormatter,"format",format)
    item=api.make("E","CARD_BLOCKED","C",datetime(2030,5,1,tzinfo=timezone.utc),{})
    service=api.create()
    api.call(service,"record",item)
    assert api.call(service,"render") == ("CONTROL",)
    assert calls == [item]
