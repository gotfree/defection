"""Программа учета брака организации
    version - 0.2.0 (27 04 2018)

    В состав модуля входят:
        [user_choice] = [
            Пересенная - триггер, хранит целочисленное значение
            для выбора пункта меню в основном цикле программы
        ],
        [how_many_goods] = [Количество товаров],
        [goods] = [Список для создания экземпляров классов],
        [again] = [
            Переменная триггер для решения продолжать работу
            в программе или нет
        ],
"""
import libs.input_validation as ipv
import libs.output_write as opw
from fillingVars.defect_vars import (CUSTOMER_DEFECT_FIELDS,
                                     GOODS_DEFECT_FIELDS, RESULT_DEFECT_FIELDS,
                                     HOW_MANY_GOODS, MENU_CHOICE_STRING,
                                     RETURN_TO_MENU, SHARP_DELIM, STAR_DELIM,
                                     WELLCOME_STRING)


def main():
    """Базовая функция программы
        инициирует главный цикл программы
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
            # Заглушка редактировать данные
            print("Ваш выбор - 2")

        elif user_choice == 3:
            # Отчет о данных в косоль
            try:
                print("\n{}\n".format(customer))
                for i in goods:
                    print(i)
            except (NameError, UnboundLocalError):
                print("Данные для отчета еще не заполненны!")

        elif user_choice == 4:
            # Запись данных в xlsx
            if len(goods) > 1:
                opw.write_poly_tables(customer, goods)
            else:
                opw.write_tables(customer, goods)

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
