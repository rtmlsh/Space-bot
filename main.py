import requests
import os
import pprint

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
path = '/Users/mac/Documents/GitHub/Space-bot/images/'
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


ensure_dir(path)
get_image(url, path, filename)


url = 'https://api.spacexdata.com/v4/launches/latest'
response = requests.get(url)
response.raise_for_status()
pprint.pprint(response.json()['links']['flickr']['original'])