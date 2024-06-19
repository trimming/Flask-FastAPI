import argparse
import time
import requests
import os
import asyncio
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


async def download(url, pathname):
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


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url

    path = urlparse(url).netloc
    img_urls = get_all_images(url)
    tasks = [asyncio.create_task(download(img_url, path))
             for img_url in img_urls]
    await asyncio.gather(*tasks)
    print(f'Общее время загрузки {time.time() - start_time:.2f} секунд')


start_time = time.time()

if __name__ == "__main__":
    asyncio.run(main())
