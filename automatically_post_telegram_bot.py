import os
import random
import time
import argparse
from dotenv import load_dotenv
from telegram import Bot
from image_handler import get_list_images, send_image

FOUR_HOURS = 14400


def post_images(bot, channel_id, periodicity=FOUR_HOURS):
    images = get_list_images()

    while True:
        if not images:
            images = get_list_images()
            random.shuffle(images)
        
        current_image = images.pop(0)
        send_image(bot, channel_id, current_image)
        
        time.sleep(periodicity)




def main():
    load_dotenv()

    TOKEN = os.getenv('TG_TOKEN')
    bot = Bot(token=TOKEN)
    channel_id = os.getenv('TG_CHAT_ID')
    periodicity = int(os.getenv('POST_PERIODICITY', ))

    parser = argparse.ArgumentParser(
        description='Automatic photo publishing.'
    )
    parser.add_argument(
        '--periodicity', 
        type=str, 
        default=FOUR_HOURS,
        help='Frequency of publications in seconds. (Default is 4 hours).'
    )

    args = parser.parse_args()
    post_images(bot, channel_id, args.periodicity)


if __name__ == '__main__':
    main()
