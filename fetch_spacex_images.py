import requests


def fetch_spacex_last_launch(last_launch_id=None):
    if last_launch_id is None:
        launch_id = 'latest'
        last_launch = fetch_launch_info(launch_id)
        last_launch_id = last_launch['id']

    last_launch_info = fetch_launch_info(last_launch_id)
    image_urls = last_launch_info['links']['flickr']['original']

    if not image_urls:
        print(
            '''No photographs were taken during the SpaceX launch. 
              Please try another ID.'''
        )
    else:
        return image_urls


def fetch_launch_info(launch_id):
    response = requests.get(
        f'https://api.spacexdata.com/v5/launches/{launch_id}'
    )
    response.raise_for_status()
    launch_info = response.json()
    return launch_info
