from abc import ABC, abstractmethod
import json

from app.support.types import event_dict

class AuditFormatter(ABC):
    @abstractmethod
    def format(self, event):
        raise NotImplementedError

class TextAuditFormatter(AuditFormatter):
    def format(self, event):
        return f'{event.event_id}|{event.event_type}|{event.entity_id}'

class JsonAuditFormatter(AuditFormatter):
    def format(self, event):
        return json.dumps(event_dict(event), ensure_ascii=False)