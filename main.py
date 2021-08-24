import requests
import os


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
path = '/Users/Алена/Documents/GitHub/Space-bot/images/'


def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        get_image(url)

def get_image(url):
    filename = '/Users/Алена/Documents/GitHub/Space-bot/images/hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


ensure_dir(path)



