import requests
import os
import argparse

from fetch_spacex_images import fetch_spacex_last_launch
from EPIC_NASA import get_earth_photo
from APOD_NASA import get_nasa_images
from pathlib import Path
from datetime import datetime
from urllib.parse import urlsplit, unquote
from datetime import datetime
from dotenv import load_dotenv


def download_images(urls, path='images'):
    folder_name = Path(path)

    try:
        folder_name.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        print(f'The folder "{folder_name}" already exists.')

    for index, url in enumerate(urls):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'image_{timestamp}_{index + 1}.jpeg'
        file_path = folder_name / filename

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
        default=30,
        help='Number of photos from NASA'
    )
    parser.add_argument(
        '--date', 
        type=str, 
        help='''Date of obtaining Earth images (no earlier than 2 days ago)''')
    args = parser.parse_args()
    image_urls = fetch_spacex_last_launch(args.id)

    if image_urls:
        download_images(image_urls, 'images/SpaceX')
    else:
        print(
        '''You can try this ID: "5eb87d47ffd86e000604b38a".
        There are definitely photos here.'''
        )

    hdurls = get_nasa_images(args.count)
    if hdurls:
        download_images(hdurls, 'images/NASA')

    image_links = get_earth_photo(args.date)
    download_images(image_links, 'images/NASA_Earth')


if __name__ == '__main__':
    main()
