import os
import random
import time
import argparse
from dotenv import load_dotenv
from telegram import Bot


def post_images(bot, channel_id, periodicity=14400):
    images = []

    for dirpath, directory, filenames in os.walk("images"):
        for filename in filenames:
            images.append(os.path.join(dirpath, filename))

    while True:
        if not images:
            for dirpath, directory, filenames in os.walk("images"):
                for filename in filenames:
                    images.append(os.path.join(dirpath, filename))
            random.shuffle(images)
        
        current_image = images.pop(0)
        size_image = os.path.getsize(current_image)

        if size_image < 20000000: 
                bot.send_photo(chat_id=channel_id, photo=open(current_image, 'rb'))

        time.sleep(periodicity)




def main():
    load_dotenv()

    TOKEN = os.getenv('TG_TOKEN')
    bot = Bot(token=TOKEN)
    channel_id = '@Home_Gamer_tg'
    periodicity = int(os.getenv('POST_PERIODICITY'))

    parser = argparse.ArgumentParser(
        description='Automatic photo publishing.'
    )
    parser.add_argument(
        '--periodicity', 
        type=str, 
        default=14400,
        help='Frequency of publications in seconds. (Default is 4 hours).'
    )

    args = parser.parse_args()
    post_images(bot, channel_id, args.periodicity)


if __name__ == '__main__':
    main()
