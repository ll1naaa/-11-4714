from app.domain.audit import AuditEvent
from app.domain.formatters import TextAuditFormatter,JsonAuditFormatter
from app.support.types import find_events,format_result,iso_timestamp


class AuditService:
    def __init__(self,repository,formatter):
        self._repository=repository
        self._formatter=TextAuditFormatter()

    def record(self,event):
        return self._repository.add(event)

    def find(self,entity_id=None,event_type=None):
        return find_events(self._repository.all(),entity_id,event_type)

    def render(self,entity_id=None,event_type=None):
        raise NotImplementedError("ЛР5: реализуйте AuditService.render по TASK.md")

    def event_counts(self, entity_id=None):
        raise NotImplementedError("ЛР5: реализуйте AuditService.event_counts по TASK.md")

    def latest_event(self, entity_id=None):
        raise NotImplementedError("ЛР5: реализуйте AuditService.latest_event по TASK.md")

def make_entity(*args, **kwargs):
    return AuditEvent(*args, **kwargs)


def invoke(service, method, *args, **kwargs):
    return getattr(service, method)(*args, **kwargs)


def view(entity):
    return {'event_id': entity.event_id, 'event_type': entity.event_type, 'entity_id': entity.entity_id, 'timestamp': entity.timestamp, 'details': entity.details}
