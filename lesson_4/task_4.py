# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.
import os
import threading
from pathlib import Path

file_dir = Path(Path.cwd(), 'download')


def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        print("Количество слов в файле " + str(file_path).split('\\')[-1] + ": " + str(len(f.read().split())))


if __name__ == '__main__':
    threads = []
    for file in os.listdir(file_dir):
        if Path(file_dir, file).is_file():
            thread = threading.Thread(target=count_words, args=(Path(file_dir, file),))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
