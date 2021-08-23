import requests
import os
import shutil

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
path = '/Users/mac/Documents/GitHub/Space-bot/image/'

def ensure_dir(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)



def get_image(url):
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


destination = os.path.split(path)
source = get_image(url)

#shutil.move(source, destination)
print(destination)