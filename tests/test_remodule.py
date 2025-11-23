import pytest

from src.remodule import process_bank_operations, process_bank_search


@pytest.fixture
def sample_data():
    return [
        {"description": "Оплата кредита"},
        {"description": "Покупка продуктов"},
        {"description": "Оплата коммунальных услуг"},
        {"description": "Перевод на карту"},
        {},
    ]


def test_process_bank_search_basic(sample_data):
    result = process_bank_search(sample_data, "оплата")
    assert len(result) == 2
    assert all("оплата" in item.get("description", "").lower() for item in result)


def test_process_bank_search_no_match(sample_data):
    result = process_bank_search(sample_data, "зарплата")
    assert result == []


# def test_process_bank_search_empty_string(sample_data):
#     # Поиск пустой строки возвращает все непустые описания
#     result = process_bank_search(sample_data, "")
#     assert len(result) == 4  # Потому что один элемент без description


def test_process_bank_operations_basic(sample_data):
    categories = ["оплата", "покупка", "перевод"]
    counts = process_bank_operations(sample_data, categories)
    assert counts["оплата"] == 2
    assert counts["покупка"] == 1
    assert counts["перевод"] == 1


def test_process_bank_operations_case_insensitive(sample_data):
    categories = ["Оплата", "ПоКупка"]
    counts = process_bank_operations(sample_data, categories)
    assert counts["Оплата"] == 2
    assert counts["ПоКупка"] == 1


def test_process_bank_operations_empty_categories(sample_data):
    counts = process_bank_operations(sample_data, [])
    assert counts == {}


def test_process_bank_operations_no_description():
    data = [{"something": "value"}]
    counts = process_bank_operations(data, ["оплата"])
    assert counts == {}
