from app.domain.formatters import AuditFormatter
from app.support.types import event_dict

class LegacyAuditAdapter(AuditFormatter):
    def __init__(self,legacy):self._legacy=legacy
    def format(self,event):
        raise NotImplementedError("Бонус: локальный форматтер")
