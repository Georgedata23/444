# Выполнил: Мальцев Георгий Павлович


import logging
import random


logging.basicConfig(level=logging.INFO, filename="py_log_2.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')



def random_generator():
    while True:
        try:
            a = int(input('left side: '))
            b = int(input('right side: '))
            if a < 0:
                raise ValueError('Используется отрицательное число!')
                logging.warning('Кто-то использует магию вне Хогвартса!')
            rn = random.randint(a, b)
        except ValueError:
            print('Неверные границы')
            logging.info('Используйте другие границы')
        except Exception:
            print("Атстой")
            logging.error("Что-то пошло не так :(")
        else:
            print(f"Случайное число в диапозоне: {rn}")
            logging.info("Получилось!")

random_generator()
