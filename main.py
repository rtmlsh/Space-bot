import telegram
import requests
import time
import os
import datetime
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_image(url, path, filename):
    image_path = f'{path}{filename}'
    response = requests.get(url)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)


def fetch_hubble_photo(path):
    filename = 'hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    get_image(url, path, filename)


def fetch_spacex_last_launch(spacex_api_url):
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    spacex_images_links = response.json()['links']['flickr']['original']
    for image_link in enumerate(spacex_images_links):
        filename = f'spacex{image_link[0]}.jpg'
        url = image_link[1]
        get_image(url, path, filename)


def fetch_nasa_day_photo(nasa_api_url, token):
    payloads = {"api_key": token, 'count': 7}
    response = requests.get(nasa_api_url, params=payloads)
    response.raise_for_status()
    for i in range(7):
        filename = f'nasa{i}{file_extension(response.json()[i]["url"])}'
        url = response.json()[i]['url']
        get_image(url, path, filename)


def fetch_epic_photo():
    response = requests.get(nasa_epic_api_url)
    response.raise_for_status()
    for i in range(7):
        date = datetime.datetime.fromisoformat(response.json()[i]['date']).\
            strftime("%Y/%m/%d")
        title = response.json()[i]['image']
        url = 'https://api.nasa.gov/EPIC/archive/natural/' \
              f'{date}/png/{title}.png?api_key=DEMO_KEY'
        filename = f'{title}.png'
        get_image(url, path, filename)


def file_extension(img_url):
    image_path = urlparse(img_url)
    image_extension = os.path.splitext(os.path.split(image_path.path)[-1])[-1]
    return image_extension


def publish_on_channel():
    while True:
        for root, dirs, files in os.walk(path):
            for filename in files:
                time.sleep(10)
                bot.send_photo(chat_id=chat_id, photo=open(f'{path}{filename}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    path = "/Users/mac/Documents/GitHub/Space-bot/images/"
    spacex_api_url = 'https://api.spacexdata.com' \
                     '/v4/launches/latest'
    nasa_api_url = 'https://api.nasa.gov/planetary/apod'
    nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/' \
                        'images?api_key=DEMO_KEY'
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    parser = argparse.ArgumentParser(
        description='Скрипт интегрируется с API NASA, SpaceX, '
                    'скачивает картинки и затем публикует их в Телеграм'
    )
    bot = telegram.Bot(token=telegram_token)
    parser.parse_args()
    ensure_dir(path)
    fetch_spacex_last_launch(spacex_api_url)
    fetch_nasa_day_photo(nasa_api_url, nasa_token)
    fetch_hubble_photo(path)
    fetch_epic_photo()
    publish_on_channel()