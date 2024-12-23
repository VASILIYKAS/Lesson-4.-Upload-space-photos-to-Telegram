import os
import requests
from datetime import datetime, timedelta


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


def get_images_info(date_url, NASA_TOKEN):
    params = {
        'api_key': NASA_TOKEN,
    }

    response = requests.get(date_url, params=params)
    response.raise_for_status()
    images_info = response.json()
    return images_info


def get_urls_earth_photo(NASA_TOKEN, formatted_date=None):
    date_url = get_date_url(formatted_date)

    images_info = get_images_info(date_url, NASA_TOKEN)

    images_urls_info = {item['date']: item['image']
                        for item in images_info if 'date' in item and 'image' in item}
    image_links = []

    for date_time, image_name in images_urls_info.items():
        date = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        formatted_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{
            formatted_date}/png/{image_name}.png?api_key={NASA_TOKEN}'
        image_links.append(image_url)
    print(image_links)
    return image_links


def main():
    NASA_TOKEN = os.environ['NASA_API_KEY']

    get_urls_earth_photo(NASA_TOKEN)


if __name__ == '__main__':
    main()
