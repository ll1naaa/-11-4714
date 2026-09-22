from app.support.types import (
    Repository, find_events,
)
from app.domain.audit import AuditEvent

class AuditService:
    def __init__(self, repository=None):
        self._repository = repository if repository is not None else Repository(
            "event_id", "DUPLICATE_EVENT"
        )

    def record(self, event):
        return self._repository.add(event)

    def find(self, entity_id=None, event_type=None):
        return find_events(
            self._repository.all(),
            entity_id=entity_id,
            event_type=event_type,
        )

    def render(self, entity_id=None, event_type=None):
        return tuple(
            f"{e.event_id}|{e.event_type}|{e.entity_id}"
            for e in self.find(entity_id=entity_id, event_type=event_type)
        )


def make_entity(event_id, event_type, entity_id, timestamp, details):
    return AuditEvent(event_id, event_type, entity_id, timestamp, details)


def invoke(service, method, *args, **kwargs):
    return getattr(service, method)(*args, **kwargs)


def view(event):
    return {
        "event_id": event.event_id,
        "event_type": event.event_type,
        "entity_id": event.entity_id,
        "timestamp": event.timestamp,
        "details": event.details,
    }


def new_service(repository=None):
    return AuditService(repository)