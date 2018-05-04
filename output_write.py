"""Модуль функций отображения и записи информации в файл
"""
import os

cwd = os.getcwd()
file_lst = os.listdir('.')
print(cwd)

for i in file_lst:
    print(i)
