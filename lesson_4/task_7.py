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
import threading



def get_sum(user_list):
    global result
    for num in user_list:
        result += num
    print(f'Сумма элементов: {result}, вычислено за {time.time() - start_time:.2f} секунд')


main_list = [i for i in range(1_000_000)]
result = 0
start_time = time.time()

if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = threading.Thread(target=get_sum, args=(main_list,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()