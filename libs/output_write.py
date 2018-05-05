"""Модуль функций отображения и записи информации в файл
"""
import xlwt
from defect_classes import Customer, Goods


"""def write_to_file(customer, goods):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('Лист1')

    cust_dict = dict(customer.__dict__)
    goods_dict = dict(goods.__dict__)

    cols = ["A", "B", "C", "D", "E"]
                data = [1, 2, 3, 4, 5]

    columns1 = list(cust_dict[0].keys())
    for i, row in enumerate(customer.__dict__):
        for j, col in enumerate(columns1):
            sheet.write(i, j, row[col])

    columns2 = list(goods_dict[0].keys())
                for i, row in enumerate(goods.__dict__):
                    for j, col in enumerate(columns2):
                        sheet.write(i, j, row[col])

    book.save('src/poly.xls')
"""

dispatch_dict = {
    'customer': 'John',
    'phone_number': '555666',
    'request_date': '24052018'
}

customer = Customer(dispatch_dict)
goods = Goods(dispatch_dict)
cust_dict = dict(customer.__dict__)
print(cust_dict)
