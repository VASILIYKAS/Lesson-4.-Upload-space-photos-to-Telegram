import os
import random
import argparse
from dotenv import load_dotenv
from telegram import Bot
from image_handler import get_list_images, send_image


def post_image(bot, channel_id, image_name=None):
    images = get_list_images()

    if not images:
        return 'No images found in the directory.'

    if image_name:
        image_path = None
        for image in images:
            if os.path.basename(image) == image_name:
                image_path = image
                break

        if image_path:
            send_image(bot, channel_id, image_path)
        else:
            return 'The image name is incorrect. Such an image was not found.'
    else:
        random_image = random.choice(images)
        send_image(bot, channel_id, random_image)


def main():
    load_dotenv()

    tg_token = os.environ['TG_TOKEN']
    bot = Bot(token=tg_token)
    channel_id = os.getenv('TG_CHAT_ID')

    parser = argparse.ArgumentParser(
        description='Manual photo publishing.'
    )
    parser.add_argument(
        '--image_name',
        type=str,
        default=None,
        help='''Specify the filename including its extension. 
        By default, a random one will be taken from the images folder.'''
    )

    args = parser.parse_args()
    
    post_image(bot, channel_id, args.image_name)


if __name__ == '__main__':
    main()
