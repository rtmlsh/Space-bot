import requests


def fetch_spacex_launch(launch_year=2018):
    spacex_api_url = 'https://api.spacexdata.com/v3/launches'
    payloads = {'launch_year': launch_year}
    response = requests.get(spacex_api_url, params=payloads)
    response.raise_for_status()
    spacex_images_links = response.json()[0]['links']['flickr_images']
    return spacex_images_links
