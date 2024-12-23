import requests
import os
import argparse

from fetch_spacex_images import fetch_spacex_last_launch
from EPIC_NASA import get_urls_earth_photo
from APOD_NASA import get_nasa_images
from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit, unquote
from datetime import datetime
from dotenv import load_dotenv


NUMBER_IMAGES = 30


def create_folder(path):
    folder_name = Path(path)
    folder_name.mkdir(parents=True, exist_ok=True)
    return folder_name


def generate_filename(index):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'image_{timestamp}_{index}.jpeg'


def generate_image_path(urls, path='images'):
    folder_name = create_folder(path)
    file_paths = []

    for index, url in enumerate(urls, start=1):
        filename = generate_filename(index)
        file_path = folder_name / filename
        file_paths.append(file_path)

    return file_paths


def download_images(urls, path='images'):
    file_paths = generate_image_path(urls, path)

    for i in range(len(urls)):
        url = urls[i]
        file_path = file_paths[i]
        response = requests.get(url)
        response.raise_for_status()

        with open(file_path, 'wb') as file:
            file.write(response.content)


def get_image_format(url):

    split_url = urlsplit(url)
    path = unquote(split_url.path)
    file_extension = os.path.splitext(path)
    return file_extension[1:]


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description='Downloading photos.'
    )
    parser.add_argument('--id', type=str, help='SpaceX launch ID')

    parser.add_argument(
        '--count',
        type=int,
        default=NUMBER_IMAGES,
        help='Number of photos from NASA'
    )

    parser.add_argument(
        '--date',
        type=str,
        help='''Date of obtaining Earth images (no earlier than 2 days ago)''')

    folder_path = os.getenv('FOLDER_PATH')

    args = parser.parse_args()
    image_urls = fetch_spacex_last_launch(args.id)

    if image_urls:
        download_images(image_urls, f'{folder_path}/SpaceX')
    else:
        print(
            '''You can try this ID: "5eb87d47ffd86e000604b38a".
        There are definitely photos here.'''
        )

    nasa_api_key = os.environ['NASA_API_KEY']

    hdurls = get_nasa_images(nasa_api_key, args.count)
    if hdurls:
        download_images(hdurls, f'{folder_path}/NASA')

    image_links = get_urls_earth_photo(nasa_api_key, args.date)
    download_images(image_links, f'{folder_path}/NASA_Earth')


if __name__ == '__main__':
    main()
