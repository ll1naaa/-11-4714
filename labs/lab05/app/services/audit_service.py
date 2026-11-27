from app.domain.audit import AuditEvent
from app.support.types import find_events, format_result


class AuditService:
    def __init__(self, repository, formatter):
        self._repository = repository
        self._formatter = formatter

    def record(self, event):
        return self._repository.add(event)

    def find(self, entity_id=None, event_type=None):
        return find_events(self._repository.all(), entity_id, event_type)

    def render(self, entity_id=None, event_type=None):
        events = self.find(entity_id=entity_id, event_type=event_type)
        results = []
        for event in events:
            formatted = self._formatter.format(event)
            results.append(format_result(formatted))
        return tuple(results)

    def event_counts(self, entity_id=None):
        counts = {}
        for event in self.find(entity_id=entity_id):
            counts[event.event_type] = counts.get(event.event_type, 0) + 1
        return counts

    def latest_event(self, entity_id=None):
        events = self.find(entity_id=entity_id)
        if not events:
            return None
        return max(events, key=lambda event: (event.timestamp, event.event_id))


def make_entity(*args, **kwargs):
    return AuditEvent(*args, **kwargs)


def invoke(service, method, *args, **kwargs):
    return getattr(service, method)(*args, **kwargs)


def view(entity):
    return {
        'event_id': entity.event_id,
        'event_type': entity.event_type,
        'entity_id': entity.entity_id,
        'timestamp': entity.timestamp,
        'details': entity.details,
    }