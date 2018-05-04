"""Модуль функций отображения и записи информации в файл
"""

import xlwt

book = xlwt.Workbook(encoding="utf-8")
sheet = book.add_sheet('Лист1')

cols = ["A", "B", "C", "D", "E"]
data = [1, 2, 3, 4, 5]

for num in range(5):
    row = sheet.row(num)
    for index, col in enumerate(cols):
        value = data[index] + num
        row.write(index, value)

book.save('src/poly.xls')
