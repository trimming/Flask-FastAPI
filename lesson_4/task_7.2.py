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
import asyncio

main_list = [i for i in range(1_000_000)]


async def get_sum(user_list):
    global result
    for num in user_list:
        result += num
    print(f'Сумма элементов: {result}, вычислено за {time.time() - start_time:.2f} секунд')


async def main():
    list_res = [main_list[i:i + 100_000] for i in range(10)]
    tasks = [asyncio.create_task(get_sum(item)) for item in list_res]
    await asyncio.gather(*tasks)


result = 0
start_time = time.time()

if __name__ == '__main__':
    asyncio.run(main())
