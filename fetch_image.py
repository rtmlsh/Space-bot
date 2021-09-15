import requests


def save_image(url, path, filename, payload=None):
    image_path = f'{path}{filename}'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(image_path, 'wb') as file:
        file.write(response.content)
