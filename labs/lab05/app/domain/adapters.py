from app.domain.formatters import AuditFormatter
from app.support.types import event_dict


class LegacyAuditAdapter(AuditFormatter):
    def __init__(self, legacy):
        self._legacy = legacy

    def format(self, event):
        return self._legacy.to_text(event_dict(event))