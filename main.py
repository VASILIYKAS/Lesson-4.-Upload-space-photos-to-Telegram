import requests
import os
import argparse
import random

from fetch_spacex_images import fetch_spacex_last_launch
from EPIC_NASA import get_urls_earth_photo
from APOD_NASA import get_nasa_images
from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit, unquote
from datetime import datetime
from dotenv import load_dotenv


def create_folder(path):
    folder_name = Path(path)
    folder_name.mkdir(parents=True, exist_ok=True)
    return folder_name


def generate_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_number = random.randint(1, 9999)
    return f'image_{timestamp}_{random_number}.jpeg'


def generate_image_path(url, path='images'):
    folder_name = create_folder(path)
    filename = generate_filename()
    file_path = folder_name / filename
    return file_path


def download_image(url, path='images'):
    file_path = generate_image_path(url, path)

    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()

    number_images = 30

    parser = argparse.ArgumentParser(
        description='Downloading photos.'
    )
    parser.add_argument('--id', type=str, help='SpaceX launch ID')

    parser.add_argument(
        '--count',
        type=int,
        default=number_images,
        help='Number of photos from NASA'
    )

    parser.add_argument(
        '--date',
        type=str,
        help='''Date of obtaining Earth images (no earlier than 2 days ago)'''
    )

    folder_path = os.getenv('FOLDER_PATH', default='images')

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

    nasa_api_key = os.environ['NASA_API_KEY']

    hdurls = get_nasa_images(nasa_api_key, args.count)
    if hdurls:
        for image in hdurls:
            download_image(image, f'{folder_path}/NASA')

    image_links = get_urls_earth_photo(nasa_api_key, args.date)
    for image in image_links:
        download_image(image, f'{folder_path}/NASA_Earth')


if __name__ == '__main__':
    main()
