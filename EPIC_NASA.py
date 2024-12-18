import os
import requests
from datetime import datetime, timedelta


def get_earth_photo(formatted_date=None):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    today_str = today.strftime('%Y.%m.%d')
    yesterday_str = yesterday.strftime('%Y.%m.%d')

    params = {
        'api_key': os.getenv('NASA_API_KEY'),
    }

    if formatted_date is None:
        date_url = 'https://api.nasa.gov/EPIC/api/natural'
    else:
        if formatted_date == today_str or formatted_date == yesterday_str:
            return print('Фотографий за сегодня и вчера ещё нет. Пожалуйста, укажите более позднюю дату.')
        
        date_url = f'https://api.nasa.gov/EPIC/api/natural/date/{formatted_date}'

    response = requests.get(date_url, params=params)
    response.raise_for_status()
    images_info = response.json()

    images_urls_info = {item['date']: item['image']
                        for item in images_info if 'date' in item and 'image' in item}
    image_links = []

    for date_time, image_name in images_urls_info.items():
        date = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        formatted_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{
            formatted_date}/png/{image_name}.png?api_key={params["api_key"]}'
        image_links.append(image_url)

    return image_links


