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
