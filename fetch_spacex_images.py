import requests


def fetch_spacex_last_launch(last_launch_id=None):
    if last_launch_id is None:
        response = requests.get(
            'https://api.spacexdata.com/v5/launches/latest'
        )
        response.raise_for_status()
        last_launch = response.json()
        last_launch_id = last_launch['id']

    response = requests.get(
        f'https://api.spacexdata.com/v5/launches/{last_launch_id}'
    )
    response.raise_for_status()
    last_launch_info = response.json()
    image_urls = last_launch_info['links']['flickr']['original']

    if not image_urls:
        print('Фотографий на запуске SpaceX не делали. Попробуйте другой id')
    else:
        return image_urls
