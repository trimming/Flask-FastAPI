# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.

import asyncio
import os
from pathlib import Path

file_dir = Path(Path.cwd(), 'download')


async def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print("Количество слов в файле " + str(file_path).split('\\')[-1] + ": " + str(len(f.read().split())))


async def main():
    tasks = [asyncio.create_task(count_words(Path(file_dir, file)))
             for file in os.listdir(file_dir)
             if Path(file_dir, file).is_file()]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
