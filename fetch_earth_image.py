import os
import requests
import configargparse

from image_downloader import download_image
from datetime import datetime, timedelta
from dotenv import load_dotenv


def get_date_str():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    today_str = today.strftime('%Y.%m.%d')
    yesterday_str = yesterday.strftime('%Y.%m.%d')
    return yesterday_str, today_str


def get_date_url(formatted_date=None):
    today_str, yesterday_str = get_date_str()

    if formatted_date is None:
        date_url = 'https://api.nasa.gov/EPIC/api/natural'
    else:
        if formatted_date == today_str or formatted_date == yesterday_str:
            return print(
                '''There are no photos available for today and yesterday. 
                Please specify a later date.'''
            )

        date_url = f'https://api.nasa.gov/EPIC/api/natural/date/{
            formatted_date}'

    return date_url


def get_images_info(date_url, nasa_api_key):
    params = {
        'api_key': nasa_api_key,
    }

    response = requests.get(date_url, params=params)
    response.raise_for_status()
    images_info = response.json()
    return images_info


def get_urls_earth_photo(nasa_api_key, formatted_date=None):
    date_url = get_date_url(formatted_date)
    images_info = get_images_info(date_url, nasa_api_key)

    images_urls_info = {item['date']: item['image']
                        for item in images_info if 'date' in item and 'image' in item}
    image_links = []

    for date_time, image_name in images_urls_info.items():
        date = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        formatted_date = date.strftime("%Y/%m/%d")

        params = {
            'api_key': nasa_api_key,
        }

        base_url = f'https://api.nasa.gov/EPIC/archive/natural/{
            formatted_date}/png/{image_name}.png'

        response = requests.get(base_url, params=params)

        image_url = response.url
        image_links.append(image_url)

    return image_links


def main():
    load_dotenv()

    folder_path = os.getenv('FOLDER_PATH', default='images')
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = configargparse.ArgParser(
        description='Download Earth photos dated on a specified date'
    )

    parser.add_argument(
        '--date',
        type=str,
        help='Date of obtaining Earth images (no earlier than 2 days ago)'
    )

    args = parser.parse_args()

    image_links = get_urls_earth_photo(nasa_api_key, args.date)

    if image_links:
        for image in image_links:
            download_image(image, f'{folder_path}/NASA_EPIC')


if __name__ == '__main__':
    main()
