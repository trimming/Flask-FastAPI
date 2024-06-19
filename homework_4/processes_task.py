import argparse
import time
import requests
import os
import threading
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


def get_all_images(url_address):
    """
    Возвращает все URL‑адреса изображений по одному `url`
    """
    soup = bs(requests.get(url_address).content, "html.parser")
    urls = []
    for image in tqdm(soup.find_all("img"), "Получено изображение"):
        image_url = image.attrs.get("src")
        if not image_url:
            # если img не содержит атрибута src, просто пропускаем
            continue
        # сделаем URL абсолютным, присоединив имя домена к только что извлеченному URL
        image_url = urljoin(url_address, image_url)
        urls.append(image_url)
    return urls


def download(url, pathname):
    """
    Загружает файл по URL‑адресу и помещает его в папку `pathname`
    """
    # если путь не существует, создать dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # загружаем тело ответа по частям, а не сразу
    response = requests.get(url, stream=True)

    # получить общий размер файла
    # file_size = int(response.headers.get("Content-Length", 0))

    # получаем имя файла
    filename = os.path.join(pathname, url.split("/")[-1])

    # индикатор выполнения, изменение единицы измерения на байты вместо итераций (по умолчанию tqdm)
    progress = tqdm(response.iter_content(1024), f"Загружен {filename} за {time.time() - start_time:.2f} секунд")

    with open(filename, "wb") as f:
        for data in progress.iterable:
            # записываем прочитанные данные в файл
            f.write(data)

            # обновление индикатора выполнения вручную
            progress.update(len(data))


# def main(url, path):
#     # получить все изображения
#     imgs = get_all_images(url)
#     for img in imgs:
#         # скачать для каждого img
#         download(img, path)
#     print(f'Общее время загрузки {time.time() - start_time:.2f} секунд')


start_time = time.time()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Этот скрипт загружает все изображения с веб‑страницы.")
    parser.add_argument("url", help="URL‑адрес веб‑страницы, с которой вы хотите загрузить изображения.")

    args = parser.parse_args()
    url = args.url

    path = urlparse(url).netloc
    # main(url, path)
    threads = []
    img_urls = get_all_images(url)
    for img_url in img_urls:
        thread = threading.Thread(target=download, args=[img_url, path])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Общее время загрузки {time.time() - start_time:.2f} секунд')