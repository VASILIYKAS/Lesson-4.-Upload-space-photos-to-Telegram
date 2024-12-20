import os
import requests


def get_nasa_images(count=10):
    if count is None or count < 1 or count > 50:
        print('Количество изображений для скачивания должно быть от 1 до 50')
        return
    
    params = {
        'api_key': os.getenv('NASA_API_KEY'),
        'count': count,
    }

    response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=params
    )

    response.raise_for_status()
    images_info = response.json()

    hdurls = [item['hdurl'] for item in images_info if 'hdurl' in item]

    return hdurls
