import argparse
import time
import telegram
from dotenv import load_dotenv
from fetch_nasa import *
from fetch_spacex import *


def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_spacex_images(spacex_images_links):
    for spacex_link in enumerate(spacex_images_links):
        filename = f'spacex{spacex_link[0]}.jpg'
        url = spacex_link[1]
        get_image(url, path, filename)


def save_nasa_day_photos(nasa_images_links):
    for nasa_link in nasa_images_links:
        filename = f'nasa{nasa_images_links.index(nasa_link)}' \
                   f'{file_extension(nasa_link)}'
        url = nasa_link
        get_image(url, path, filename)


def save_epic_photos(epic_photo_links):
    for epic_title, epic_link in epic_photo_links.items():
        url = epic_link
        filename = f'{epic_title}.png'
        get_image(url, path, filename)


def get_image(url, path, filename):
    image_path = f'{path}{filename}'
    response = requests.get(url)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)


def publish_on_channel():
    while True:
        for root, dirs, files in os.walk(path):
            for filename in files:
                time.sleep(86400)
                bot.send_photo(
                    chat_id=chat_id,
                    photo=open(f'{path}{filename}', 'rb')
                )


if __name__ == '__main__':
    load_dotenv()
    path = 'C:/Users/Алена/Documents/GitHub/Space-bot/images/'
    spacex_api_url = 'https://api.spacexdata.com/v3/launches'
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
    spacex_images_links = fetch_spacex_last_launch(spacex_api_url)
    save_spacex_images(spacex_images_links)
    nasa_images_links = fetch_nasa_day_photo(nasa_token, nasa_api_url)
    save_nasa_day_photos(nasa_images_links)
    epic_photo_links = fetch_epic_photo(nasa_epic_api_url)
    save_epic_photos(epic_photo_links)
    publish_on_channel()
