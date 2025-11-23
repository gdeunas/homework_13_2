from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(cards: str) -> str:
    """Принимать один аргумент — строку, содержащую тип
    и номер карты или счета.
    Аргументом может быть строка типа
    Visa Platinum 7000792289606361, или
    Maestro 7000792289606361, или
    Счет 73654108430135874305.
    Разделять строку на 2 аргумента (отдельно имя,
    отдельно номер) нельзя!"""
    if cards is None:  #
        return ""  #
    elif str(cards[0:4]) == "Счет":  #
        card_show = cards[6:]
        card_text = cards[0:5] + get_mask_account(card_show)
    else:
        card_items = cards.split(" ")
        card_type = ""
        card_num = ""
        for card_item in card_items:
            if card_item.isalpha():
                card_type += card_item + " "
            elif card_item.isdigit():
                card_num = card_item
        card_num = get_mask_card_number(card_num)
        card_text = card_type + card_num
    return card_text


def get_date(long_dates: str) -> str:
    """которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    short_date = ""
    for i in range(0, 10):
        short_date += long_dates[i]
        i += 1
    y, m, d = short_date.split("-")
    # ru_short_date = '"ДД.ММ.ГГГГ"'+'("'+d+'.'+m+'.'+y+'")'
    ru_short_date = d + "." + m + "." + y

    return ru_short_date
