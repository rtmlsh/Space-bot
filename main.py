import requests
import os

img_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
path = '/Users/mac/Documents/GitHub/Space-bot/images/'
spacex_api_url = 'https://api.spacexdata.com/v4/launches/latest'
filename = 'hubble.jpeg'

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



ensure_dir(path)
get_image(img_url, path, filename)
fetch_spacex_last_launch(spacex_api_url)