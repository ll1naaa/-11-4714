from app.support.types import identifier, choice, utc_seconds, details_copy, EVENT_TYPES


class AuditEvent:
    def __init__(self,event_id,event_type,entity_id,timestamp,details):
        self._event_id=identifier(event_id)
        self._event_type=choice(event_type,EVENT_TYPES,"INVALID_EVENT_TYPE")
        self._entity_id=identifier(entity_id)
        self._timestamp=utc_seconds(timestamp)
        self._details=details_copy(details)

    @property
    def event_id(self):return self._event_id

    @property
    def event_type(self):return self._event_type

    @property
    def entity_id(self):return self._entity_id

    @property
    def timestamp(self):return self._timestamp

    @property
    def details(self):return dict(self._details)
