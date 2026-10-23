from abc import ABC, abstractmethod
import json
from app.support.types import event_dict


class AuditFormatter(ABC):
    @abstractmethod
    def format(self,event) -> str:
        raise NotImplementedError


class TextAuditFormatter(AuditFormatter):
    def __init__(self, separator="|"):
        self._separator = separator
    def format(self, event) -> str:
        return self._separator.join((event.event_id, event.event_type, event.entity_id))


class JsonAuditFormatter(AuditFormatter):
    def format(self,event) -> str:
        return json.dumps(event_dict(event), ensure_ascii=False)
