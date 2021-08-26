import requests
import os
import datetime
from urllib.parse import urlparse
import pprint

path = '/Users/Алена/Documents/GitHub/Space-bot/images/'
spacex_api_url = 'https://api.spacexdata.com/v4/launches/latest'
nasa_api_url = 'https://api.nasa.gov/planetary/apod'
nasa_epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
nasa_token = 'ZBsB0Y1t6U4PxTL1iL7nNlIYLqKzlsBWRzlZxZMw'
img_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
filename = 'hubble.jpeg'

# /Users/Алена/Documents/GitHub/Space-bot/images/
# /Users/mac/Documents/GitHub/Space-bot/images/

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


def fetch_spacex_last_launch(spacex_api_url):
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    spacex_images = response.json()['links']['flickr']['original']
    for images_links in enumerate(spacex_images):
        filename = f'spacex{images_links[0]}.jpg'
        url = images_links[1]
        get_image(url, path, filename)


def fetch_nasa_day_photo(nasa_api_url, nasa_token):
    payloads = {"api_key": nasa_token, 'count': 7}
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
        date = datetime.datetime.fromisoformat(response.json()[i]['date']).strftime("%Y/%m/%d")
        title = response.json()[i]['image']
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{title}.png?api_key=DEMO_KEY'
        filename = f'{title}.png'
        get_image(url, path, filename)


def file_extension(img_url):
    image_path = urlparse(img_url)
    image_extension = os.path.splitext(os.path.split(image_path.path)[-1])[-1]
    return image_extension


ensure_dir(path)
get_image(img_url, path, filename)
fetch_spacex_last_launch(spacex_api_url)
fetch_nasa_day_photo(nasa_api_url, nasa_token)
fetch_epic_photo()
