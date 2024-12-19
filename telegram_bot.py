import os
from dotenv import load_dotenv
from telegram import Bot, InputMediaDocument


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
# bot.send_message(chat_id=channel_id, text="Тестовое сообщение@")
bot.send_document(chat_id=channel_id, document=open('images/NASA/image_20241218_175029_2.jpeg', 'rb')) # Отправка без сжатия
bot.send_photo(chat_id=channel_id, photo=open('images/NASA/image_20241218_175029_2.jpeg', 'rb')) # Отправка с сжатием

