"""Модуль функций для проверки значений и вывода информации

В состав модуля входят:
    [start_info] -- [Вывод стартовой информации о программе]
    [menu_prompt] -- [Интерфейс главного меню программы]
    [user_choice_validation] -- [Функция выбора пункта меню]
    [quantity_of_goods_validation] -- [
        Функция записи и проверки количества сдаваемых товаров
    ]
    [again_choice] -- [Функция подтверждения возврата в главное меню]
"""


def start_info(delimiter, wellcome_string):
    """Вывод строки приветствия

    Args:
        delimiter (str): Символьный разделитель
        wellcome_string (str): Текст приветствия
    """
    print("\n\n{0}\n{1}\n{0}".format((delimiter * 2), wellcome_string))


def menu_prompt(delimiter):
    """Представление пунктов меню

    Args:
        delimiter (str): Символьный разделитель
    """
    print(("\n{}\nВыберете необходимую операцию:\n"
           "1. Записать информацию о покупателе и браке\n"
           "2. Редактировать данные перед записью\n"
           "3. Вывести отчет\n"
           "4. Записать данные в файл\n"
           "5. Создать файл\n"
           "6. Выход\n".format(delimiter * 2)))


def user_choice_validation(arg):
    """Пользовательский ввод и проверка
    пунктов меню

    Args:
        arg (str): Строка - выбор пункта меню

    Returns:
        int: Значение пользовательского ввода, число для
        выбора пункта меню
    """
    while True:
        try:
            value = int(input(arg))
        except ValueError:
            print("Введите целое число")
            continue
        else:
            if value not in range(1, 7):
                print("Введите число от 1 до 6")
            else:
                break
    return value


def quantity_of_goods_validation(arg):
    """Пользовательский ввод и проверка
    значения количества здаваемых товаров по браку

    Args:
        arg (str): Строка - выбор количества товаров

    Returns:
        int: Значение пользовательского ввода, количество
        сдаваемых по браку товаров
    """
    while True:
        try:
            value = int(input(arg))
        except ValueError:
            print("Введите целое число")
            continue
        else:
            if value not in range(1, 10):
                print("Введите число от 1 до 10")
            else:
                break
    return value


def again_choice(arg):
    """Функция подтверждения возврата в главное меню

    Args:
        arg (str): Приглашение вернуться в главное
        меню

    Returns:
        str: Значение пользовательского ввода,
        подтверждение возврата в главное меню
    """
    while True:
        value = input(arg).lower()
        if value not in {'да', 'нет'}:
            print("Введите 'да' или 'нет'")
        else:
            break
    return value
