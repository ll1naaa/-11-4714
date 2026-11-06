from abc import ABC, abstractmethod
import json
from app.support.types import event_dict


class AuditFormatter(ABC):
    @abstractmethod
    def format(self,event):
        raise NotImplementedError


class TextAuditFormatter(AuditFormatter):
    def format(self,event):
        return legacy_l4_textauditformatter_format(self, event)


class JsonAuditFormatter(AuditFormatter):
    def format(self,event):
        return legacy_l4_jsonauditformatter_format(self, event)


# ЛР4: временный процедурный путь. Перенесите реализацию в названный метод объекта и удалите эту функцию.
def legacy_l4_textauditformatter_format(owner, event):
    return f'{event.event_id}|{event.event_type}|{event.entity_id}'


# ЛР4: временный процедурный путь. Перенесите реализацию в названный метод объекта и удалите эту функцию.
def legacy_l4_jsonauditformatter_format(owner, event):
    return json.dumps(event_dict(event), ensure_ascii=False)
