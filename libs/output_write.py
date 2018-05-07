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


def write_tables(arg1, arg2):
    """
    Добавить вариант заполнения в случае, когда у контрагента
    больше одного товара
        - Значения первого словаря из goods, записать как
        в ветке else
        - Значения поледующих словарей записать аналогично, но
        вместо инфо о покупателе записать None ячейки

    добавить автоматическую шрину ячейки
    """
    if len(arg2) > 1:
        print("Запись нескольких товаров, скоро появится")
        """
            count = 0
            for x in arg2:
                x[count].write....
                count += 1
        """
    else:
        value_list = list(arg1.values()) + list(arg2[0].values())

        dest_file = 'output/test.xlsx'
        wb = openpyxl.load_workbook(dest_file)
        ws = wb.active

        next_col = 1
        row_num = ws.max_row + 1
        for i in value_list:
            ws.cell(column=next_col, row=row_num, value=i)
            next_col += 1

        wb.save(filename=dest_file)
