# Выполнил: Мальцев Георгий Павлович

import logging

# a = [x for x in input('Введите числа: ').split(sep=',')]

logging.basicConfig(level=logging.INFO, filename="py_log_3.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')


def mid_arif(a):
    try:
        if isinstance(a, list) == False:
            logging.info("Неправильный ввод")
            raise TypeError('Неподходящий тип данных, используйте список')
    except TypeError:
        print("Используйте другой тип данных(list)")
    except Exception:
        logging.error('Неизведанная ошибка')
    else:
        for i in a:
            try:
                if isinstance(i, int) == False:
                    raise TypeError("Необходимо вводить только числа")
                    logging.warning("Человек не вводит цифры")
            except TypeError:
                return print("Используйте цифры без кавычек и скобок внутри списка")
        for i in a:
            x = 0
            x += i
        print(f"Среднее арифметическое: {x/len(a)}")
        logging.info("Succsesfull!!!")



mid_arif(123)



