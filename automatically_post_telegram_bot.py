import os
import random
import time
import configargparse
from dotenv import load_dotenv
from telegram import Bot
from image_handler import get_list_images, send_image

FOUR_HOURS = 14400


def post_images(bot, channel_id, folder_path='images', periodicity=FOUR_HOURS):
    images = get_list_images(folder_path)

    while True:
        if not images:
            images = get_list_images(folder_path)
            random.shuffle(images)

        if not images:
            print("No images found in the directory.")
            break

        current_image = images.pop(0)

        send_image(bot, channel_id, current_image)

        time.sleep(periodicity)


def main():
    load_dotenv()

    TOKEN = os.environ['TG_TOKEN']
    bot = Bot(token=TOKEN)
    channel_id = os.environ['TG_CHAT_ID']

    parser = configargparse.ArgParser()

    parser.add(
        '--periodicity',
        type=int,
        default=int(os.getenv('POST_PERIODICITY', FOUR_HOURS)),
        help='Frequency of publications in seconds (Default is 4 hours).'
    )
    parser.add(
        '--path',
        default=os.getenv('FOLDER_PATH', 'images'),
        help='Path to the folder containing images'
    )

    config = parser.parse_args()

    folder_path = config.path
    periodicity = config.periodicity

    post_images(bot, channel_id, folder_path, periodicity)


if __name__ == '__main__':
    main()
