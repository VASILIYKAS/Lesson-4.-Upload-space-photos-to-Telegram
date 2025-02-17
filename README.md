# NASA & SpaceX Image Publisher Bot

This project consists of a Telegram bot that automatically publishes images to a specified Telegram channel at a set interval. The bot publishes all images located in the images folder, including subdirectories. Images can be added either manually or by running functions that automatically download pictures from the following sources:

* SpaceX: Retrieves images from the latest launch.
* NASA APOD: Fetches the Astronomy Picture of the Day.
* NASA EPIC: Provides daily photos of Earth.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Environment Variables](#Environment-Variables)
- [Usage](#usage)
  - [Default Values](#Default-Values)
- [API Functions](#api-functions)
  - [NASA API](#nasa-api)
  - [SpaceX API](#spacex-api)
- [Telegram Bot](#telegram-bot)
- [Project goal](#project-goal)

## Features

- Fetch images from NASA and SpaceX APIs.
- Publish images to a Telegram channel at a specified interval.
- Handle image size limitations (only images smaller than 20 MB are published).
- Randomly reshuffle images once all have been posted.

## Requirements

- Python 3.12.6
- `python-telegram-bot` library
- `requests` library
- `python-dotenv` library
- `configargparse` library
- `urllib3` library


## Installation

1. Clone the repository:

```bash
git clone https://github.com/VASILIYKAS/Lesson-4.-Upload-space-photos-to-Telegram.git
cd Lesson-4.-Upload-space-photos-to-Telegram
```
Install the required packages:

```bash
pip install -r requirements.txt
```
### Environment Variables
Create a .env file in the root directory and add your Telegram bot token and other environment variables:

`TG_TOKEN=your_telegram_bot_token` # You can get it here [BotFather](https://telegram.me/BotFather).\
`POST_PERIODICITY=14400`  # Time in seconds between posts.\
`NASA_API_KEY=your_nasa_token` # You can get it here [NASA API](https://api.nasa.gov/).\
`TG_CHAT_ID=сhat_id_of_your_channel` # You can find it out through bot [userinfobot](https://telegram.me/userinfobot) by forwarding any message from your channel to it. In response, the bot will write the first line: the username (or nickname) starts with the @ sign, which can be used as chat_id, and the second line is the same chat_id but in numbers, which always starts with a "minus" sign. For example:
```
TG_CHAT_ID=@example_tg or TG_CHAT_ID=-1001112223334
```
`FOLDER_PATH=images` The name of the folder where images will be downloaded, by default it is `images`, but you can change it to any other folder.

`LAUNCH_ID=launch-id` # Please specify the ID of the launch you are interested in. The default is set to "5eb87d47ffd86e000604b38a".

`IMAGES_COUNT=number` # Please specify the number of images to download, from 1 to 100. The default is set to 30.
## Usage
To run the bot, execute the following command:
```bash
python automatically_post_telegram_bot.py
```
When you run this command, the bot will start publishing all images available in the `images` folder at an interval of 4 hours.\
\
For downloading images, there are three scripts available:
```bash
fetch_spacex_images.py
```
Downloads photos from the latest SpaceX rocket launch. Alternatively, you can specify your own launch ID (note that SpaceX does not always provide photos from every launch).
```bash
fetch_nasa_image_of_the_day.py
```
Downloads a specified number (default is 30) of "images of the day".
```bash
fetch_earth_image.py
```
Downloads Earth images for a specified date (default is the latest available).
### Default Values
In this case, default values will be used:

- For SpaceX rocket launches: The default will be the latest launch. Sometimes photographs are not taken during a launch, so you can specify the ID of another launch:
```bash
python fetch_spacex_images.py --id number-id
```
You can see the launch ID number [here](https://api.spacexdata.com/v5/launches). At the end of each launch, there is a line with the ID, for example: "id": "5eb87d47ffd86e000604b38a".

- For NASA's Astronomy Picture of the Day (APOD): You can specify the number of pictures. The default is set to 30, but to change it (with a maximum of 100), enter the command:
```bash
python fetch_nasa_image_of_the_day.py --count number-of-pictures
```

- For NASA's EPIC: You can specify a date in the format YYYY.MM.DD to retrieve Earth photographs from that day. If no date is provided, the date two days prior will be used:
```bash
python fetch_earth_image.py --date date
```
- For the image publishing bot, you can specify the posting frequency. By default, it is set to every 4 hours.
```bash
python automatically_post_telegram_bot.py --periodicity Frequency-in-seconds
```
And the selection of the folder from which the images will be published. By default, it is set to "images," but you can change it to any other folder.
```bash
python automatically_post_telegram_bot.py --path Your-path-to-the-folder
```
- For the bot that sends an image by its name, there is also a default value. If you do not specify the name of the image, a random image from the images folder will be sent.
```bash
python post_telegram_bot.py --image_name The-name-of-the-image-including-its-extension
```
## API Functions
### NASA API
The function responsible for generating image links from the NASA API fetches images related to space exploration. You can customize the API endpoint or parameters as needed.

### SpaceX API
Similarly, the function for the SpaceX API retrieves images related to SpaceX missions and launches. This function can also be modified to adjust the data fetched from the API.

## Telegram Bot
The Telegram bot is implemented in two files. One is needed for periodically sending images to the specified channel. The other is for manually sending images to the channel by the filename:

- Periodically sending images to a specified Telegram channel.
- Reshuffling the image list once all images have been sent.
- Manual sending of an image or a random image to the specified Telegram channel.

## Project goal
Code written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).


