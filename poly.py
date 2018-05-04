"""
    Генератор словаря с обходом кортежа заготовленных переменных
    и инициализацией их значений с помощью форматированного
    пользовательского ввода
    main_dict = {k: str(input("Set {}: ".format(k)))
             for k in defect_vars.MAIN_DEFECT_FIELDS}
    for k, v in main_dict.items():
            print('{}\n{} -- {}'.format(defect_vars.STAR_DELIM, k, v))
"""

"""Механизм инициации классов значениями словарей

class allMyFields(object):
    # note: you cannot (and don't have to) use self here
    Field1 = None
    Field2 = None

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

q = { 'Field1' : 3000, 'Field2' : 6000, 'RandomField' : 5000 }
instance = allMyFields(q)

print instance.Field1      # => 3000
print instance.Field2      # => 6000
print instance.RandomField # => 5000
"""
