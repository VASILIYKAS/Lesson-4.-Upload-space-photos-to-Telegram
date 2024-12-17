import requests
import os
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
        print(f'Папка "{folder_name}" уже существует.')

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


def get_30_nasa_images():
    params = {
        'api_key': os.getenv('NASA_API_KEY'),
        'count': 30,
    }

    response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=params
    )

    response.raise_for_status()
    images_info = response.json()

    hdurls = [item['hdurl'] for item in images_info if 'hdurl' in item]

    return hdurls


def get_earth_photo():
    params = {
        'api_key': os.getenv('NASA_API_KEY'),
    }

    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural', params=params
    )
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


def main():
    load_dotenv()
    image_urls = fetch_spacex_last_launch()
    download_images(image_urls, 'images/SpaceX')
    hdurls = get_30_nasa_images()
    download_images(hdurls, 'images/NASA')
    image_links = get_earth_photo()
    download_images(image_links, 'images/NASA_Earth')


if __name__ == '__main__':
    main()
