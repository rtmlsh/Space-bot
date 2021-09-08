import requests
import os
import datetime
from urllib.parse import urlparse
from fetch_image import save_image


def fetch_nasa_day_photo(nasa_token, number_images):
    nasa_api_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': 7}
    response = requests.get(nasa_api_url, params=payload)
    response.raise_for_status()
    nasa_images_links = []
    for num in range(number_images):
        nasa_images_links.append(response.json()[num]["url"])
    return nasa_images_links


def fetch_epic_photo(nasa_token, number_images):
    nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_token}
    response = requests.get(nasa_epic_api_url, params=payload)
    response.raise_for_status()
    epic_api_json = response.json()
    epic_photo_links = {}
    for num in range(number_images):
        date = datetime.datetime.fromisoformat(epic_api_json[num]['date'])\
            .strftime('%Y/%m/%d')
        title = epic_api_json[num]['image']
        link = 'https://api.nasa.gov/EPIC/archive/natural/' \
               f'{date}/png/{title}.png'
        epic_photo_links[title] = requests.get(link, params=payload).url
    return epic_photo_links


def file_extension(img_url):
    image_path = urlparse(img_url)
    image_extension = os.path.splitext(os.path.split(image_path.path)[-1])[-1]
    return image_extension


def save_nasa_day_photos(nasa_images_links, path='images/'):
    for num, nasa_link in enumerate(nasa_images_links):
        filename = f'nasa{num}{file_extension(nasa_link)}'
        save_image(nasa_link, path, filename)


def save_epic_photos(epic_photo_links, path='images/'):
    for epic_title, epic_link in epic_photo_links.items():
        filename = f'{epic_title}.png'
        save_image(epic_link, path, filename)



