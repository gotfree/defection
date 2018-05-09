"""Модуль функций отображения и записи информации в файл
"""
import openpyxl


def create_file(arg1, arg2, arg3):
    head_list = arg1 + arg2 + arg3

    dest_file = 'output/test.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.freeze_panes = 'A2'

    next_col = 1
    for i in head_list:
        ws.cell(column=next_col, row=1, value=i)
        next_col += 1

    wb.save(filename=dest_file)


def write_poly_tables(arg1, arg2):
    """
    Добавить вариант заполнения в случае, когда у контрагента
    больше одного товара
        - Значения первого словаря из goods, записать как
        в ветке else
        - Значения поледующих словарей записать аналогично, но
        вместо инфо о покупателе записать None ячейки

    добавить автоматическую шрину ячейки
    """
    dest_file = 'output/test.xlsx'
    none_list = [None, None, None]

    # Записаль информацию о первом товаре
    value_poly_list = list(arg1.values()) + list(arg2[0].values())
    wpb = openpyxl.load_workbook(dest_file)
    wps = wpb.active

    next_col = 1
    row_num = wps.max_row + 1
    for i in value_poly_list:
        wps.cell(column=next_col, row=row_num, value=i)
        next_col += 1

    wpb.save(filename=dest_file)
    # Весь код выше заменить вызывом функции write_tables()

    # "вытолкнули" первый элемент списка
    arg2.pop(0)
    for x in arg2:
        pass
        """
        записать поочередно словарь из None и значений goods
        в последующие строки
        """
    print("Запись нескольких товаров, скоро появится")
    """
    count = 0
    for x in arg2:
        x[count].write....
        count += 1
    """


def write_tables(arg1, arg2):
    dest_file = 'output/test.xlsx'
    value_list = list(arg1.values()) + list(arg2[0].values())
    wb = openpyxl.load_workbook(dest_file)
    ws = wb.active

    next_col = 1
    row_num = ws.max_row + 1
    for i in value_list:
        ws.cell(column=next_col, row=row_num, value=i)
        next_col += 1

    wb.save(filename=dest_file)
