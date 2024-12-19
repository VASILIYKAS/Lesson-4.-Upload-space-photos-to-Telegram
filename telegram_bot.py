import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

TOKEN = os.getenv('TG_TOKEN')
bot = Bot(token=TOKEN)
info_bot = bot.get_me()

bot_info = {
    'id': info_bot.id,
    'first_name': info_bot.first_name,
    'is_bot': info_bot.is_bot,
    'username': info_bot.username
}

print(bot_info)

channel_id = '@Home_Gamer_tg'
bot.send_message(chat_id=channel_id, text="Тестовое сообщение@")

