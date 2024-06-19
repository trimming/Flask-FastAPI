# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import time
import multiprocessing


def get_sum(user_list, cnt):
    for num in user_list:
        with cnt.get_lock():
            cnt.value += num
    print(f'Сумма элементов: {cnt.value:_}, вычислено за {time.time() - start_time:.2f} секунд')


main_list = [i for i in range(1_000_000)]
result = multiprocessing.Value('l', 0)
start_time = time.time()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=get_sum, args=(main_list[:500_000], result))
    p2 = multiprocessing.Process(target=get_sum, args=(main_list[500_000:], result))
    p1.start()
    p2.start()
