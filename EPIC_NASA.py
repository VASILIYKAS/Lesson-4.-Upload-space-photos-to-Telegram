import os
import requests
from datetime import datetime, timedelta
from urllib.parse import urlencode
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
    
        base_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{image_name}.png'
        image_url = f"{base_url}?{urlencode(params)}"
        image_links.append(image_url)
    return image_links


def main():
    load_dotenv()
    
    nasa_api_key = os.environ['NASA_API_KEY']

    get_urls_earth_photo(nasa_api_key)


if __name__ == '__main__':
    main()
