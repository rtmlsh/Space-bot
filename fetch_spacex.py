import requests


def fetch_spacex_last_launch(spacex_api_url):
    payloads = {'launch_year': '2018'}
    response = requests.get(spacex_api_url, params=payloads)
    response.raise_for_status()
    spacex_images_links = response.json()[0]['links']['flickr_images']
    return spacex_images_links




