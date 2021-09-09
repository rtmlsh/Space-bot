import requests


def save_image(url, path, filename, params=None):
    url = requests.get(url, params=params).url
    image_path = f'{path}{filename}'
    response = requests.get(url)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)
