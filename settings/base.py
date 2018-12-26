"""Модуль переменных для defective_doods.py

    В состав модуля входят:
        [CUSTOMER_DEFECT_FIELDS]--[Кортеж с полями 'Покупатель' для заполнения]
        [GOODS_DEFECT_FIELDS] -- [Кортеж с полями 'Товар' для заполнения]
        [RESULT_DEFECT_FIELDS] -- [Кортеж с полями 'Результат' для заполнения]
        [STAR_DELIM] -- [Строка для символа-разделителя '*']
        [SHARP_DELIM] -- [Строка для символа-разделителя '#']
        [WELLCOME_STRING] -- [Строка приветствия]
        [MENU_CHOICE_STRING] -- [Строка выбора пункта меню]
        [RETURN_TO_MENU] -- [Строка - приглашение возврата в главное меню]
        [HOW_MANY_GOODS] -- [Строка запроса количества товаров]
        [BASE_DIR] -- [Корневая директория программы]
        [PATH_SEP] -- [Кроссплатформенный разделитель для путя]
        [DEST_FILE] -- [Название]

    элементы кортежей используются для заполнения полей словаря,
    было принято решение именовать строками на русском языке
"""
import os
from pathlib import Path

BASE_DIR = Path().resolve()
PATH_SEP = os.sep
DEST_FILE = 'output{}'.format(PATH_SEP)
OUTPUT_PATH = os.path.join(BASE_DIR, DEST_FILE)


CUSTOMER_DEFECT_FIELDS = (
    'Покупатель',
    'Номер телефона',
    'Дата обращения'
)

GOODS_DEFECT_FIELDS = (
    'Код товара',
    'Наименование',
    'Количество',
    'Номер документа',
    'Неисправность',
    'Товарный вид'
)

RESULT_DEFECT_FIELDS = (
    'Результат диагностики',
    'Статус товара'
)

STAR_DELIM = "**********************"
SHARP_DELIM = "######################"
WELLCOME_STRING = "Учет брака от покупателей (версия - 0.4.0)"
MENU_CHOICE_STRING = "Пункт меню №: "
RETURN_TO_MENU = "Вернуться в главное меню?(да/нет) "
HOW_MANY_GOODS = "Сколько товаров сдается по браку? "


if __name__ == '__main__':
    print("base dir - {0}\n{1}\n{2}".format(BASE_DIR,
                                            PATH_SEP,
                                            OUTPUT_PATH))
