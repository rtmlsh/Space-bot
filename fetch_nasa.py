import datetime
import os
from urllib.parse import urlparse

import requests

from fetch_image import save_image


def fetch_nasa_day_photos(nasa_token, number_images):
    nasa_api_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': number_images}
    response = requests.get(nasa_api_url, params=payload)
    response.raise_for_status()
    nasa_images_links = []
    for image in response.json():
        nasa_images_links.append(image['url'])
    return nasa_images_links


def fetch_epic_photos(nasa_token, number_images):
    nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_token}
    response = requests.get(nasa_epic_api_url, params=payload)
    response.raise_for_status()
    epic_photo_links = {}
    for image in response.json()[:number_images]:
        date = datetime.datetime.fromisoformat(image['date'])\
            .strftime('%Y/%m/%d')
        title = image['image']
        epic_photo_links[title] = 'https://api.nasa.gov/EPIC/archive/natural/'\
                                  f'{date}/png/{title}.png'
    return epic_photo_links


def get_file_extension(img_url):
    image_path = urlparse(img_url)
    image_extension = os.path.splitext(image_path.path)[-1]
    return image_extension


def save_nasa_day_photos(nasa_images_links, path='images/'):
    for num, nasa_link in enumerate(nasa_images_links):
        filename = f'nasa{num}{get_file_extension(nasa_link)}'
        save_image(nasa_link, path, filename)


def save_epic_photos(nasa_token, epic_photo_links, path='images/'):
    for epic_title, epic_link in epic_photo_links.items():
        filename = f'{epic_title}.png'
        save_image(epic_link, path, filename, payload={'api_key': nasa_token})
