import json
from app.domain.audit import AuditEvent
from app.support.types import find_events,event_dict,iso_timestamp


class AuditService:
    def __init__(self,repository,mode="text"):
        self._repository=repository
        self._mode=mode

    def record(self,event):
        return self._repository.add(event)

    def find(self,entity_id=None,event_type=None):
        return find_events(self._repository.all(),entity_id,event_type)

    def render(self,entity_id=None,event_type=None):
        events=self.find(entity_id,event_type)
        if self._mode=="json":
            return tuple(json.dumps(event_dict(e),ensure_ascii=False) for e in events)
        return tuple(f"{e.event_id}|{e.event_type}|{e.entity_id}" for e in events)

def make_entity(*args, **kwargs):
    return AuditEvent(*args, **kwargs)


def invoke(service, method, *args, **kwargs):
    return getattr(service, method)(*args, **kwargs)


def view(entity):
    return {'event_id': entity.event_id, 'event_type': entity.event_type, 'entity_id': entity.entity_id, 'timestamp': entity.timestamp, 'details': entity.details}


from app.support.types import Repository,choice

def new_service(repository=None,mode="text"):
    choice(mode,("text","json"),"INVALID_CONFIG")
    return AuditService(repository if repository is not None else Repository("event_id","DUPLICATE_EVENT"),mode)
