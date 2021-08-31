import requests
import os
import datetime
from urllib.parse import urlparse


def fetch_nasa_day_photo(nasa_token, nasa_api_url):
    payloads = {"api_key": nasa_token, 'count': 7}
    response = requests.get(nasa_api_url, params=payloads)
    response.raise_for_status()
    nasa_images_links = []
    for i in range(6):
        nasa_images_links.append(response.json()[i]["url"])
    return nasa_images_links


def fetch_epic_photo(nasa_epic_api_url):
    response = requests.get(nasa_epic_api_url)
    response.raise_for_status()
    epic_photo_links = {}
    for i in range(6):
        date = datetime.datetime.fromisoformat(response.json()[i]['date']).\
            strftime("%Y/%m/%d")
        title = response.json()[i]['image']
        epic_photo_links[title] = 'https://api.nasa.gov/EPIC/archive/natural/' \
              f'{date}/png/{title}.png?api_key=DEMO_KEY'
    return epic_photo_links


def file_extension(img_url):
    image_path = urlparse(img_url)
    image_extension = os.path.splitext(os.path.split(image_path.path)[-1])[-1]
    return image_extension




