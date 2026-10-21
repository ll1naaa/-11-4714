# Audit: справка для ЛР3

Событие содержит время, тип, идентификаторы и снимок деталей. Форматтер превращает событие в строку, не изменяя журнал.

Здесь перечислены типы текущей работы. Что требуется реализовать и какие файлы можно менять, указано в [TASK.md](TASK.md).

## Предметные объекты и исполнители

| Тип и конструктор | Публичные действия и свойства | Файл |
|---|---|---|
| `AuditEvent(event_id, event_type, entity_id, timestamp, details)` | `event_id`, `event_type`, `entity_id`, `timestamp`, `details` | `app/domain/audit.py` |
| `AuditFormatter()` | `format(event)` | `app/domain/formatters.py` |
| `TextAuditFormatter()` | `format(event)` | `app/domain/formatters.py` |
| `JsonAuditFormatter()` | `format(event)` | `app/domain/formatters.py` |

Свойства читаются без скобок. Поля объекта-значения не меняются присваиванием; результат операции создаётся отдельно. Для наследника без собственного конструктора показаны аргументы конструктора базового класса.

## Вызов сервиса

| Метод | Сигнатура |
|---|---|
| `__init__` | `AuditService(repository, formatter)` |
| `record` | `record(event)` |
| `find` | `find(entity_id=None, event_type=None)` |
| `render` | `render(entity_id=None, event_type=None)` |

`app/api.py` — готовая внешняя граница; не изменяйте её. Вызов попадает в сервис из указанного модуля. Подробные примеры создания входных объектов находятся в открытых тестах текущей папки.

Состав исполнителей в этой заготовке задан. Функция сборки уже готова; `app/services/assembly.py` не меняется. Задача — реализовать общий вызов и распределить поведение между указанными объектами.

## Готовые результаты и ошибки

`DomainError` находится в `app/support/errors.py`; код доступен через `error.code`. В разрешённых методах используйте готовые проверки, а не новую иерархию исключений.

Допустимые типы событий: `PAYMENT_APPROVED`, `PAYMENT_DECLINED`, `CARD_BLOCKED`, `LIMIT_CHANGED`. Временная метка — `datetime` в UTC с точностью до секунд. `format_result()` проверяет строковый результат, иначе `INVALID_FORMAT_RESULT`.

## Проверка поведения

`tests/test_contract.py` и `tests/test_review_contract.py` проверяют предметные правила. `tests/test_progression.py` проверяет последовательности обращений и настройки текущей работы. Ни один результат теста не является командой менять защищённый API или тесты.

Ожидаемый стартовый результат — в [STARTER-STATE.md](STARTER-STATE.md). Проверка из корня проекта: `python check.py lab03`.
