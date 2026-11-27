from app.services.audit_service import AuditService
from app.support.types import Repository, choice
from app.domain.formatters import TextAuditFormatter, JsonAuditFormatter


def build_service(repository=None, formatter=None, mode="text"):
    choices = {"text": TextAuditFormatter, "json": JsonAuditFormatter}
    choice(mode, choices, "INVALID_CONFIG")

    selected_formatter = choices[mode]() if formatter is None else formatter
    selected_repository = (
        Repository("event_id", "DUPLICATE_EVENT")
        if repository is None
        else repository
    )

    return AuditService(selected_repository, selected_formatter)