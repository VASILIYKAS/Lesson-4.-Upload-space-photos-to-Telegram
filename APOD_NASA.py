import os
import requests


MIN_IMAGES = 1
MAX_IMAGES = 100


def get_nasa_images(nasa_api_key, count=30):
    if count is None or count < MIN_IMAGES or count > MAX_IMAGES:
        print('The number of images to download must be between 1 and 100')
        return

    params = {
        'api_key': nasa_api_key,
        'count': count,
    }

    response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=params
    )

    response.raise_for_status()
    images_info = response.json()

    hdurls = [item['hdurl'] for item in images_info if 'hdurl' in item]

    return hdurls


def main():
    nasa_api_key = os.getenv('NASA_API_KEY')
    get_nasa_images(nasa_api_key)


if __name__ == '__main__':
    main()