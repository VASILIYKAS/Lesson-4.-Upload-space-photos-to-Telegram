import os
import requests
import configargparse

from dotenv import load_dotenv
from image_downloader import download_image


def get_nasa_images(nasa_api_key, count=30):
    min_images = 1
    max_images = 100
    
    if count is None or count < min_images or count > max_images:
        print('The number of images to download must be between 1 and 100')
        return

    params = {
        'api_key': nasa_api_key,
        'count': count,
    }

    response = requests.get(
        'https://api.nasa.gov/planetary/apod', params=params
    )

    response.raise_for_status()
    images_info = response.json()

    hdurls = [item['hdurl'] for item in images_info if 'hdurl' in item]

    return hdurls


def main():
    load_dotenv()

    folder_path = os.getenv('FOLDER_PATH', default='images')
    nasa_api_key = os.environ['NASA_API_KEY']
    
    parser = configargparse.ArgParser(
        description='Download the photo of the day from the NASA website.'
    )

    parser.add_argument(
        '--count',
        type=int,
        default=os.getenv('IMAGES_COUNT', 30),
        help='Please specify the number of photos for download'
    )

    args = parser.parse_args()

    hdurls = get_nasa_images(nasa_api_key, args.count)

    if hdurls:
        for image in hdurls:
            download_image(image, f'{folder_path}/NASA_APOD')

if __name__ == '__main__':
    main()