import random

from pathlib import Path
from datetime import datetime


def create_folder(path):
    folder_name = Path(path)
    folder_name.mkdir(parents=True, exist_ok=True)
    return folder_name


def generate_filename():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_number = random.randint(1, 9999)
    return f'image_{timestamp}_{random_number}.jpeg'


def generate_image_path(url, path='images'):
    folder_name = create_folder(path)
    filename = generate_filename()
    file_path = folder_name / filename
    return file_path



