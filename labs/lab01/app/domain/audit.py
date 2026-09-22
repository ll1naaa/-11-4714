from dataclasses import dataclass
from datetime import datetime
from app.support.types import details_copy, EVENT_TYPES, identifier, utc_seconds
from app.support.errors import DomainError


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    event_type: str
    entity_id: str
    timestamp: datetime
    details: dict

    def __post_init__(self):
        if self.event_type not in EVENT_TYPES:
            raise DomainError("INVALID_CONTEXT")
        object.__setattr__(self, "event_id", identifier(self.event_id))
        object.__setattr__(self, "entity_id", identifier(self.entity_id))
        object.__setattr__(self, "timestamp", utc_seconds(self.timestamp))
        object.__setattr__(self, "details", details_copy(self.details))

    def describe(self) -> str:
        return f"{self.event_id}:{self.event_type}:{self.entity_id}"