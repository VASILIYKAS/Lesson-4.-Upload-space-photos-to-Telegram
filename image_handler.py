import os
from telegram import Bot


TWENTY_MEGABYTES = 20000000


def get_list_images(folder_path='images'):
    images = []
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for dirpath, directory, filenames in os.walk(folder_path):
            for filename in filenames:
                images.append(os.path.join(dirpath, filename))

        if not images:
            return 'The folder is empty'

    else:
        return 'The folder with images does not exist!'
    return images


def send_image(bot, channel_id, image_path):
    size_image = os.path.getsize(image_path)
    if size_image < TWENTY_MEGABYTES:
        with open(image_path, 'rb') as photo:
            bot.send_photo(chat_id=channel_id, photo=photo)
    else:
        return f'The size of the image {os.path.basename(image_path)} exceeds 20 MB.'