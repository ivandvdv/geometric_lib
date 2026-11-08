# История изменений

История изменений проекта geometric_lib.

## 8ba9aeb — L-03: Circle and square added

Добавлены модули `circle.py` и `square.py` с функциями площади и периметра.

## d078c8d — L-03: Docs added

Добавлен первый вариант документации `docs/README.md` с формулами.

## 44151ee — Add rectangle.py

Добавлен модуль `rectangle.py`.

## 1e18dd1 — Add triangle.py and fix rectangle perimeter

Добавлен модуль `triangle.py` и исправлена формула периметра прямоугольника.

## 7b2905e — add comments

Добавлены комментарии к функциям.

## 372c526 — add docs

Обновлено описание проекта в `docs/README.md`.

## 9855391 — L-04: Add docstrings to all functions

Комментарии заменены на docstring во всех функциях: описание, параметры, возвращаемое значение и пример.

## 6603cbd — L-04: Update documentation for all modules

Обновлена документация в каталоге `docs`: общее описание с формулами, описание функций (`functions.md`) и история изменений (`history.md`).

## L-06: Add unit tests for all figures

Добавлены unit-тесты на `unittest` для всех четырёх фигур: `test_circle.py`, `test_square.py`, `test_rectangle.py`, `test_triangle.py` (35 тестов). Проверяются площадь и периметр на обычных, нулевых и дробных значениях, а также реакция на некорректные данные. Исходный код фигур не изменялся. Запуск: `python3 -m unittest -v`.
