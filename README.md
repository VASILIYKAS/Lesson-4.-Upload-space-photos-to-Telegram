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
- `urllib3` library
- `python-dotenv` library
- `pathlib` library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/VASILIYKAS/Lesson-4.-Upload-space-photos-to-Telegram.git
cd repository-name
```
Install the required packages:

```bash
pip install -r requirements.txt
```
### Environment Variables
Create a .env file in the root directory and add your Telegram bot token and other environment variables:

`TG_TOKEN=your_telegram_bot_token` # You can get it here [BotFather](https://telegram.me/BotFather).\
`POST_PERIODICITY=14400`  # Time in seconds between posts.\
`NASA_API_KEY=your_nasa_token` # You can get it here [NASA API](https://api.nasa.gov/).
## Usage
To run the bot, execute the following command:
```bash
python post_telegram_bot.py
```
To download images, use the following command:
```bash
python main.py
```
### Default Values
In this case, default values will be used:

- For SpaceX rocket launches: The default will be the latest launch. Sometimes photographs are not taken during a launch, so you can specify the ID of another launch:
```bash
python main.py --id number-id
```
- For NASA's Astronomy Picture of the Day (APOD): You can specify the number of pictures. The default is set to 30, but to change it (with a maximum of 100), enter the command:
```bash
python main.py --count number-of-pictures
```
- For NASA's EPIC: You can specify a date in the format YYYY.MM.DD to retrieve Earth photographs from that day. If no date is provided, the date two days prior will be used:
```bash
python main.py --date date
```
## API Functions
### NASA API
The function responsible for generating image links from the NASA API fetches images related to space exploration. You can customize the API endpoint or parameters as needed.

### SpaceX API
Similarly, the function for the SpaceX API retrieves images related to SpaceX missions and launches. This function can also be modified to adjust the data fetched from the API.

## Telegram Bot
The Telegram bot is implemented in a separate file and is responsible for:

- Periodically sending images to a specified Telegram channel.
- Checking image sizes before sending to ensure they meet the size requirements.
- Reshuffling the image list once all images have been sent.

## Project goal
Code written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/).


