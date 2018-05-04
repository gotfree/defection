"""Модуль классов для defective_doods.py

    В состав модуля входят классы:
        [Customer] -- [Класс описывает Контрагента]
        [Goods] -- [Класс описывает Товар]
        [Result] -- [Класс описывает Решение по заявке на брак]
"""


class Customer():
    """Класс с информацией о покупателе, для учета брака предприятия
    """

    def __init__(self, dict):
        self.__dict__.update(dict)

    def __str__(self):
        """Простое представление класса
        """
        return "{}".format(self.__dict__)


class Goods():
    """Класс с информацией о товаре, для учета брака предприятия
    """

    def __init__(self, dict):
        self.__dict__.update(dict)

    def __str__(self):
        """Простое представление класса
        """
        return "{}".format(self.__dict__)


class Result():
    """Класс для сбора информации о браке, для учета брака предприятия
    """

    def __init__(self, dict):
        self.__dict__.update(dict)

    def __str__(self):
        """Простое представление класса
        """
        return "{}".format(self.__dict__)


def main():
    dispatch_dict = {
        'customer': 'John',
        'phone_number': '555666',
        'request_date': '24052018'
    }

    instance1 = Customer(dispatch_dict)
    instance2 = Goods(dispatch_dict)
    instance3 = Result(dispatch_dict)

    print("{}\n{}\n{}".format(instance1, instance2, instance3))


if __name__ == '__main__':
    main()
