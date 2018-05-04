"""Модуль функций отображения и записи информации в файл

import os

cwd = os.getcwd()
file_lst = os.listdir('.')
print(cwd)

for i in file_lst:
    print(i)
"""
import pandas as pd
from openpyxl import load_workbook

wb = load_workbook('src/sheet.xlsx')
sheet = wb.get_sheet_by_name('Лист1')

df = pd.DataFrame(sheet.values)

print(df)
