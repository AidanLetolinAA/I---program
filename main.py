"""Простой пример программы для знакомства с Python.

Скрипт показывает базовые конструкции: функции, условия, циклы и работу
с аргументами командной строки. Запустите файл напрямую или через
```
python main.py --name "Имя"
```
"""

import argparse
from datetime import datetime


def build_greeting(name: str, excited: bool = False) -> str:
    """Собрать приветствие с именем и текущей датой.

    Args:
        name: Имя пользователя.
        excited: Добавить ли восклицательный знак.
    """
    suffix = "!" if excited else "."
    today = datetime.now().strftime("%d.%m.%Y")
    return f"Привет, {name}! Сегодня {today}{suffix}"


def sum_numbers(limit: int) -> int:
    """Сложить числа от 1 до limit включительно."""
    total = 0
    for number in range(1, limit + 1):
        total += number
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Мини-пример для новичков")
    parser.add_argument(
        "--name", default="друг", help="Имя для приветствия (по умолчанию 'друг')"
    )
    parser.add_argument(
        "--excited",
        action="store_true",
        help="Добавить восклицательный знак к приветствию",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="До какого числа считать сумму (по умолчанию 5)",
    )

    args = parser.parse_args()

    greeting = build_greeting(args.name, args.excited)
    total = sum_numbers(args.limit)

    print(greeting)
    print(f"Сумма от 1 до {args.limit}: {total}")


if __name__ == "__main__":
    main()
