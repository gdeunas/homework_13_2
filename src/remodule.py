import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка. При реализации этой функции
    используйте библиотеку re для работы с регулярными выражениями."""
    pattern = re.compile(search, re.IGNORECASE)
    result = []
    for item in data:
        if pattern.search(item.get("description", "")):
            result.append(item)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и
    список категорий операций, а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description."""
    counter: dict = Counter()
    for item in data:
        description = item.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1
    return dict(counter)
