import json
from app.support.types import event_dict
from app.domain.audit import AuditEvent
from app.domain.formatters import TextAuditFormatter,JsonAuditFormatter
from app.support.types import find_events,format_result,iso_timestamp


class AuditService:
    def __init__(self,repository,formatter):
        self._repository=repository
        self._formatter=formatter

    def record(self,event):
        return self._repository.add(event)

    def find(self,entity_id=None,event_type=None):
        return find_events(self._repository.all(),entity_id,event_type)

    def render(self,entity_id=None,event_type=None):
        events=find_events(self._repository.all(),entity_id,event_type)
        if isinstance(self._formatter,JsonAuditFormatter):
            return tuple(json.dumps(event_dict(e),ensure_ascii=False) for e in events)
        return tuple(f"{e.event_id}|{e.event_type}|{e.entity_id}" for e in events)

    def timestamp_text(self,event):
        return event.timestamp.isoformat()

def make_entity(*args, **kwargs):
    return AuditEvent(*args, **kwargs)


def invoke(service, method, *args, **kwargs):
    return getattr(service, method)(*args, **kwargs)


def view(entity):
    return {'event_id': entity.event_id, 'event_type': entity.event_type, 'entity_id': entity.entity_id, 'timestamp': entity.timestamp, 'details': entity.details}


from app.support.types import Repository,choice
from app.domain.formatters import TextAuditFormatter,JsonAuditFormatter

def new_service(repository=None,formatter=None,mode="text"):
    choices={"text":TextAuditFormatter,"json":JsonAuditFormatter}
    choice(mode,choices,"INVALID_CONFIG")
    formatter=choices[mode]() if formatter is None else formatter
    return AuditService(repository if repository is not None else Repository("event_id","DUPLICATE_EVENT"),formatter)
