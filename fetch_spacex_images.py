import requests
import configargparse
import os

from main import download_image
from dotenv import load_dotenv


def fetch_spacex_last_launch(last_launch_id='5eb87d47ffd86e000604b38a'):
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


def main():
    load_dotenv()
    folder_path = os.getenv('FOLDER_PATH', default='images')

    parser = configargparse.ArgumentParser(description='Downloading photos from spacex.')
    parser.add_argument(
        '--id',
        default=os.getenv('LAUNCH_ID', '5eb87d47ffd86e000604b38a'),
        help='SpaceX launch ID'
    )

    args = parser.parse_args()

    image_urls = fetch_spacex_last_launch(args.id)

    if image_urls:
        for image in image_urls:
            download_image(image, f'{folder_path}/SpaceX')
    else:
        print(
            '''You can try this ID: "5eb87d47ffd86e000604b38a".
        There are definitely photos here.'''
        )


if __name__ == '__main__':
    main()
