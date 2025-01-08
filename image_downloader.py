import requests
import image_utils


def download_image(url, path='images'):
    file_path = image_utils.generate_image_path(url, path)

    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)