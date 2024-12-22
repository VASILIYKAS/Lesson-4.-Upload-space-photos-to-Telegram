import os
import random
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

    TOKEN = os.getenv('TG_TOKEN')
    bot = Bot(token=TOKEN)
    channel_id = os.getenv('TG_CHAT_ID')
    post_image(bot, channel_id)


if __name__ == '__main__':
    main()
