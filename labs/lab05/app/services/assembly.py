from app.services.audit_service import AuditService
from app.support.types import Repository,choice
from app.domain.formatters import TextAuditFormatter,JsonAuditFormatter

_shared=Repository("event_id","DUPLICATE_EVENT")

def build_service(repository=None,formatter=None,mode="text"):
    choices={"text":TextAuditFormatter,"json":JsonAuditFormatter}
    choice(mode,choices,"INVALID_CONFIG")
    formatter=choices[mode]() if formatter is None else formatter
    return AuditService(repository if repository is not None else _shared,formatter)
