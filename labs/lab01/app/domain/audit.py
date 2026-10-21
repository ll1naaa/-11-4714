from datetime import datetime
from app.support.types import details_copy, EVENT_TYPES, identifier, utc_seconds
from app.support.errors import DomainError


class AuditEvent:
    def __init__(self, event_id, event_type, entity_id, timestamp, details):
        if event_type not in EVENT_TYPES:
            raise DomainError("INVALID_CONTEXT")
        self.event_id = identifier(event_id)
        self.event_type = event_type
        self.entity_id = identifier(entity_id)
        self.timestamp = utc_seconds(timestamp)
        self._details = details_copy(details)

    @property
    def details(self):
        return dict(self._details)

    def describe(self):
        return f"{self.event_id}:{self.event_type}:{self.entity_id}"