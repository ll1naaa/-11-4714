from abc import ABC, abstractmethod
import json
from app.support.types import event_dict


class AuditFormatter:
    def format(self,event):
        raise NotImplementedError


class TextAuditFormatter(AuditFormatter):
    def format(self,event):
        return ""  # ЛР3: текст


class JsonAuditFormatter(AuditFormatter):
    def format(self,event):
        return ""  # ЛР3: JSON
