# Исходные проверки ЛР5

Успешных проверок: **11**. Ожидаемых падений: **8**.

Не завершены использование переданных зависимостей, сборка и основной путь операции. Проверки вызывают разные конфигурации и ошибающегося исполнителя; ошибка не должна превращаться в успешный результат или повторную операцию.

Падения ниже связаны с конкретными требованиями [TASK.md](TASK.md). После обязательной части все они должны пройти. Бонус проверяется отдельно и не входит в эти числа.

## Новые последовательности и конфигурации

- `tests.test_progression::test_progression_audit_snapshot_duplicate_then_success`
- `tests.test_progression::test_progression_extra_lab05`
- `tests.test_progression::test_progression_false_formatter_error_does_not_delete_event`

## Предметный контракт и общий интерфейс

- `tests.test_contract::test_filters_are_combined`
- `tests.test_contract::test_formatter_injection_and_shared_repository`
- `tests.test_contract::test_independent_empty_repository`
- `tests.test_contract::test_record_find_order_and_supplied_time`
- `tests.test_contract::test_render_failure_does_not_delete_record`

## Порядок проверки

Из корня проекта: `python check.py lab05`. Сначала прочитайте первый traceback и ожидаемый результат сценария. Не отключайте тесты, которые пока не проходят.

Ошибка импорта или установки не относится к заданию. Если исходный набор результатов отличается, сохраните вывод и сообщите преподавателю; не удаляйте решения и служебные файлы.
