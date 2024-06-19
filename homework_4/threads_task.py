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
    Возвращает все URL‑адреса изображений по одному введенному в консоли URL-адресу
    """
    soup = bs(requests.get(url_address).content, "html.parser")
    urls = []
    for image in tqdm(soup.find_all("img"), "Получено изображение"):
        image_url = image.attrs.get("src")
        if not image_url:
            continue
        image_url = urljoin(url_address, image_url)
        urls.append(image_url)
    return urls


def download(url, pathname):
    """
    Загружает изображение по URL‑адресу и сохраняет его в папку `pathname`
    """
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    filename = os.path.join(pathname, url.split("/")[-1])
    progress = tqdm(response.iter_content(1024), f"Загружен {filename} за {time.time() - start_time:.2f} секунд")

    with open(filename, "wb") as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))


start_time = time.time()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url

    path = urlparse(url).netloc
    threads = []
    img_urls = get_all_images(url)
    for img_url in img_urls:
        thread = threading.Thread(target=download, args=[img_url, path])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Общее время загрузки {time.time() - start_time:.2f} секунд')
