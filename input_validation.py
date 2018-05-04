"""Модуль функций для проверки значений и вывода информации

В состав модуля входят:
    [start_info] -- [Вывод стартовой информации о программе]
    [menu_prompt] -- [Интерфейс главного меню программы]
    [user_choice_validation] -- [Функция проверки пользовательского ввода]
    [again_choice] -- [Функция проверки пользовательского ввода]
"""


def start_info(delimiter, wellcome_string):
    print("\n\n{0}\n{1}\n{0}".format((delimiter*2), wellcome_string))


def menu_prompt(delimiter):
    print(("\n{}\nВыберете необходимую операцию:\n"
           "1. Записать информацию о покупателе и браке\n"
           "2. Редактировать существующие записи\n"
           "3. Вывести отчет\n"
           "4. Записать данные в файл\n"
           "5. Выход\n".format(delimiter*2)))


def user_choice_validation(arg):
    """[Пользовательский ввод с проверкой значений в цикле]
    Arguments:
        arg {[str]} -- [
            Строка приглашения для ввода значения пункта меню
        ]
    Returns:
        [int] -- [Целое число для выбора пункта меню]
    """
    while True:
        try:
            value = int(input(arg))
        except ValueError:
            print("Введите целое число")
            continue
        else:
            if value not in range(1, 6):
                print("Введите число от 1 до 5")
            else:
                break
    return value


def quantity_of_goods_validation(arg):
    """[Пользовательский ввод с проверкой значений в цикле]
    Arguments:
        arg {[str]} -- [
            Строка приглашения для ввода значения пункта меню
        ]
    Returns:
        [int] -- [Целое число для выбора пункта меню]
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
    """[Пользовательский ввод с проверкой значений в цикле]
    Arguments:
        arg {[str]} -- [
            Строка - предложение вернуться в главное меню
        ]
    Returns:
        [str] -- [Возвращает или 'да' или 'нет']
    """
    while True:
        value = input(arg).lower()
        if value not in {'да', 'нет'}:
            print("Введите 'да' или 'нет'")
        else:
            break
    return value
