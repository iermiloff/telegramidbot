import os
import telebot

# Читаем токен напрямую из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Критическая ошибка: Переменная окружения BOT_TOKEN не задана!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь или перешли мне медиафайл (фото, видео, гиф, аудио, документ), и я вышлю его ID.")

@bot.message_handler(content_types=['photo', 'video', 'video_note', 'voice', 'audio', 'animation', 'document'])
def handle_media(message):
    file_id = None
    media_type = message.content_type

    if media_type == 'photo':
        file_id = message.photo[-1].file_id
    elif media_type == 'animation':
        file_id = message.animation.file_id
    elif media_type == 'video':
        file_id = message.video.file_id
    elif media_type == 'video_note':
        file_id = message.video_note.file_id
    elif media_type == 'voice':
        file_id = message.voice.file_id
    elif media_type == 'audio':
        file_id = message.audio.file_id
    elif media_type == 'document':
        file_id = message.document.file_id

    if file_id:
        # Моноширинный текст для копирования в один клик
        bot.reply_to(message, f"`{file_id}`", parse_mode='Markdown')
    else:
        bot.reply_to(message, "Не удалось определить ID файла.")

if __name__ == '__main__':
    print("Бот успешно запущен внутри Docker-контейнера...")
    bot.infinity_polling()
