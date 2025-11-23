from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> Union[str]:
    """
    Функция get_mask_card_number
    принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры,
    остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
    Пример работы функции:
    7000792289606361     # входной аргумент
    7000 79** **** 6361  # выход функции
    """
    # check is card_number is number
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")

    # default values
    new_number = ""
    i = 0

    # if numbers, then convert numbers to stars
    # check length of card number (=16)
    if card_number.isdigit() and len(card_number) == 16:
        # print("digits")
        while i <= len(card_number):
            if i < 6:
                new_number += card_number[i]
            elif i < 12:
                new_number += "*"
            elif i < 16:
                new_number += card_number[i]
            i += 1
    # add " " after each 4th char
    new_number = " ".join(new_number[i * 4 : (i + 1) * 4] for i in range(4))
    # else:
    #    print("no digits")
    return new_number


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция get_mask_account
    принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера,
    а перед ними — две звездочки. Пример работы функции:
    73654108430135874305  # входной аргумент
    **4305  # выход функции"""
    # check card_number is number
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")

    # reduce account_number to 6 digits
    account_number = account_number[-6:]

    # default values
    new_number = ""
    i = 0

    # if numbers, then convert numbers to stars
    if account_number.isdigit():
        # print("digits")
        while i <= len(account_number):
            if i < 2:
                new_number += "*"
            elif i < 6:
                new_number += account_number[i]
            i += 1
    # else:
    #    print("no digits")
    return new_number


# test
# number = 7000792289606361
# print(get_mask_card_number(number))
#
# account = "73654108430135874305"
# print(get_mask_account(account))
