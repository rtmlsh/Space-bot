import argparse
import time
import os
import telegram
from dotenv import load_dotenv
from fetch_nasa import fetch_nasa_day_photo, fetch_epic_photo,\
    save_nasa_day_photos, save_epic_photos
from fetch_spacex import fetch_spacex_launch, save_spacex_images


def ensure_dir(path):
    if os.makedirs(path, exist_ok=False):
        os.makedirs(path)


def publish_on_channel():
    while True:
        for root, dirs, files in os.walk(path):
            for filename in files:
                time.sleep(86400)
                with open(f'{path}{filename}', 'rb') as file:
                    bot.send_photo(chat_id=chat_id, photo=file)


if __name__ == '__main__':
    load_dotenv()
    path = 'images/'
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
    save_spacex_images(spacex_images_links=fetch_spacex_launch())
    save_nasa_day_photos(nasa_images_links=fetch_nasa_day_photo(nasa_token))
    save_epic_photos(epic_photo_links=fetch_epic_photo(nasa_token))
    publish_on_channel()
