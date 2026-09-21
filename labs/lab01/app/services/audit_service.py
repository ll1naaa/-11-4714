from app.support.types import find_events


def make_entity(event_id,event_type,entity_id,timestamp,details):
    return dict(event_id=event_id,event_type=event_type,entity_id=entity_id,timestamp=timestamp,details=dict(details))


def _new_legacy_service(repository):return {"repository":repository}

def view(event):return dict(event)


def invoke(service,method,*args,**kwargs):
    repository=service["repository"]
    if method=="record":return repository.add(args[0])
    events=find_events(repository.all(),*args,**kwargs)
    if method=="find":return events
    if method=="render":return tuple(f"{e['event_id']}|{e['event_type']}|{e['entity_id']}" for e in events)
    raise ValueError(method)


from app.support.types import Repository

def new_service(repository=None):
    return _new_legacy_service(repository if repository is not None else Repository("event_id","DUPLICATE_EVENT"))
