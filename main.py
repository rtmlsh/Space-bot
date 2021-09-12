import argparse
import os
import time

import telegram
from dotenv import load_dotenv

from fetch_nasa import (fetch_epic_photos, fetch_nasa_day_photos,
                        save_epic_photos, save_nasa_day_photos)
from fetch_spacex import fetch_spacex_launch, save_spacex_images


def publish_on_channel(path):
    while True:
        for root, dirs, files in os.walk(path):
            for filename in files:
                time.sleep(86400)
                with open(f'{path}{filename}', 'rb') as file:
                    bot.send_photo(chat_id=chat_id, photo=file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скрипт интегрируется с API NASA, SpaceX, '
                    'скачивает картинки и затем публикует их в Телеграм'
    )
    parser.parse_args()

    path = 'images/'
    os.makedirs(path, exist_ok=False)

    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')

    save_spacex_images(spacex_images_links=fetch_spacex_launch())
    save_nasa_day_photos(
        nasa_images_links=fetch_nasa_day_photos(nasa_token, number_images=6)
    )
    save_epic_photos(
        epic_photo_data=fetch_epic_photos(nasa_token, number_images=6)
    )

    bot = telegram.Bot(token=telegram_token)
    publish_on_channel(path)
