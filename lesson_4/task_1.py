# Задание №1
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.
from pathlib import Path

import requests
import threading
import time

urls = ['https://www.google.ru/',
        'https://www.yandex.ru/',
        'https://www.gb.ru/',
        'https://www.python.org/',
        'https://www.mail.ru/'
        'https://www.sportcast.ru/',
        'https://www.rutube.ru/',
        'https://www.mpstats.ru/',
        'https://www.github.com/',
        'https://www.habr.com/'
        ]


def download(url):
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    file_path = Path(path_download, filename)
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


if __name__ == '__main__':
    path_download = Path(Path.cwd(), 'download')
    if not path_download.is_dir():
        path_download.mkdir(parents=True, exist_ok=True)

    threads = []
    start_time = time.time()

    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
