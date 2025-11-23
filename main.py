from pathlib import Path

import pandas as pd

from src.import_data import read_csv, read_xl
from src.remodule import process_bank_search
from src.utils import json_filter
from src.widget import mask_account_card


def main():
    """main func"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    current_file = Path(__file__).resolve()
    directory = current_file.parent
    file_json = directory / "data" / "operations.json"
    file_csv = directory / "data" / "transactions.csv"
    file_xl = directory / "data" / "transactions_excel.xlsx"
    data = []

    user_choice_file = input()
    if user_choice_file == "1":
        print("Для обработки выбран JSON-файл.")
        data = json_filter(file_json)
    elif user_choice_file == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_csv(file_csv)
    elif user_choice_file == "3":
        print("Для обработки выбран XLSX-файл.")
        data = read_xl(file_xl)
    else:
        print("Необходимо выбрать 1,2 или 3.")

    status = ""
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while status not in valid_statuses:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if status in valid_statuses:
            print(f"Операции отфильтрованы по статусу '{status}'")
            break
        else:
            print(f"Статус операции '{status}' недоступен")

    filtered_data = []
    for item in data:
        if item.get("state", "") == status:
            filtered_data.append(item)

    sort_by_date_yn = input("Отсортировать операции по дате? Да/Нет").lower()
    if sort_by_date_yn == "да":
        sort_by_asc = input("Отсортировать по возрастанию или по убыванию?").lower()
        if sort_by_asc == "по убыванию":
            reverse = True
        else:
            reverse = False
        filtered_data.sort(key=lambda x: x.get("date"), reverse=reverse)

    sort_by_rub_yn = input("Выводить только рублевые транзакции? Да/Нет").lower()
    if sort_by_rub_yn == "да":
        filtered_data_rub = []
        for item in filtered_data:
            if item.get("currency_code") == "RUB":
                filtered_data_rub.append(item)
        filtered_data = filtered_data_rub

    filter_by_text_yn = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет."
    ).lower()
    if filter_by_text_yn == "да":
        filter_by_text = input("Введите слово для фильтра")
        filtered_data = process_bank_search(filtered_data, filter_by_text)

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
    for item in filtered_data:
        date = (
            pd.to_datetime(item.get("date")).strftime("%d.%m.%Y")
            if item.get("date")
            else ""
        )
        desc = item.get("description", "")
        item_from = mask_account_card(str(item.get("from", "")))
        item_to = mask_account_card(str(item.get("to", "")))
        if user_choice_file == "1":
            amount = str(item["operationAmount"].get("amount", ""))
            currency = item["operationAmount"]["currency"].get("code", "")
        else:
            amount = str(item.get("amount", ""))
            currency = item.get("currency_code", "")
        print(f"{date} {desc}")
        if pd.isna(item.get("from", "")) or not item.get("from", ""):
            print(f"{item_to}")
        else:
            print(f"{item_from} -> {item_to}")
        print(f"Сумма: {amount} {currency}\n")


main()
