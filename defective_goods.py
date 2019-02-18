"""Программа учета брака организации
    version - 0.2.0 (27 04 2018)
    version - 0.3.0 (09 05 2018)
    version - 0.4.0 (10 05 2018)

    В состав программы входят:
        [user_choice] -- [Строка хранит выбор пункта меню]
        [how_many_goods] -- [Строка хранит количество товаров]
        [customer] -- [Словарь с информацией о контрагенте]
        [goods] -- [Список словарей с информацией о товарах]
"""
import libs.input_validation as ipv
import libs.output_write as opw
from settings.base import (CUSTOMER_DEFECT_FIELDS,
                           RESULT_DEFECT_FIELDS, GOODS_DEFECT_FIELDS,
                           HOW_MANY_GOODS, MENU_CHOICE_STRING,
                           RETURN_TO_MENU, SHARP_DELIM, STAR_DELIM,
                           WELLCOME_STRING)


def main():
    """Базовая функция программы инициирует главный цикл
    """

    # сводка о программе
    ipv.start_info(STAR_DELIM, WELLCOME_STRING)

    while True:
        ipv.menu_prompt(SHARP_DELIM)

        # выбор пункта меню
        user_choice = ipv.user_choice_validation(MENU_CHOICE_STRING)
        if user_choice == 6:
            # Выход
            break

        elif user_choice == 1:
            # Сбор данных
            customer = {k: str(input("Заполните поле {}: ".format(k)))
                        for k in CUSTOMER_DEFECT_FIELDS}
            how_many_goods = ipv.quantity_of_goods_validation(HOW_MANY_GOODS)
            goods = []
            for i in range(how_many_goods):
                print("Товар: ", i + 1)
                goods.append({k: str(input("Заполните поле {}: ".format(k)))
                              for k in GOODS_DEFECT_FIELDS})

        elif user_choice == 2:
            # Заглушка "редактировать данные"
            print("Ваш выбор - 2")

        elif user_choice == 3:
            # Отчет о данных в консоль
            try:
                print("\n{}\n".format(customer))
                for i in goods:
                    print(i)
            except (NameError, UnboundLocalError):
                print("Данные для отчета еще не заполненны!")

        elif user_choice == 4:
            # Запись данных в файл
            try:
                if len(goods) > 1:
                    opw.write_poly_tables(customer, goods)
                else:
                    opw.write_tables(customer, goods)
            except (NameError, UnboundLocalError):
                print("Данные для записи не были инициализированны!")

        elif user_choice == 5:
            # Создание нового файла
            opw.create_file(CUSTOMER_DEFECT_FIELDS,
                            GOODS_DEFECT_FIELDS,
                            RESULT_DEFECT_FIELDS)

        # возврат в главное меню
        again = ipv.again_choice(RETURN_TO_MENU)
        if again not in {'да'}:
            break
        else:
            continue


if __name__ == '__main__':
    main()
