# Исходные проверки ЛР3

Успешных проверок: **9**. Ожидаемых падений: **7**.

Не завершены общий интерфейс, алгоритмы исполнителей и основной метод сервиса. Поэтому один незаполненный метод может вызвать несколько падений — это не несколько независимых задач.

Падения ниже связаны с конкретными требованиями [TASK.md](TASK.md). После обязательной части все они должны пройти. Бонус проверяется отдельно и не входит в эти числа.

## Новые последовательности и конфигурации

- `tests.test_progression::test_progression_audit_snapshot_duplicate_then_success`

## Предметный контракт и общий интерфейс

- `tests.test_contract::test_abc_is_abstract`
- `tests.test_contract::test_filters_are_combined`
- `tests.test_contract::test_record_find_order_and_supplied_time`
- `tests.test_contract::test_text_and_json_preserve_data`
- `tests.test_review_contract::test_review_json_contains_all_event_fields`
- `tests.test_review_contract::test_review_service_uses_formatter_in_lab3`

## Порядок проверки

Из корня проекта: `python check.py lab03`. Сначала прочитайте первый traceback и ожидаемый результат сценария. Не отключайте тесты, которые пока не проходят.

Ошибка импорта или установки не относится к заданию. Если исходный набор результатов отличается, сохраните вывод и сообщите преподавателю; не удаляйте решения и служебные файлы.
