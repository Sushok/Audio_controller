import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler
from controller import Controller

# Загружаем переменные окружения из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Обработчики команд
async def play_pause(update: Update, context):
    Controller.play_pause()
    await update.message.reply_text("⏯ Музыка: Play/Pause")

async def next_track(update: Update, context):
    Controller.next_track()
    await update.message.reply_text("⏭ Следующий трек")

async def prev_track(update: Update, context):
    Controller.prev_track()
    await update.message.reply_text("⏮ Предыдущий трек")

async def volume_up(update: Update, context):
    Controller.volume_up()
    await update.message.reply_text("🔊 Громкость увеличена")

async def volume_down(update: Update, context):
    Controller.volume_down()
    await update.message.reply_text("🔉 Громкость уменьшена")

async def mute(update: Update, context):
    Controller.mute()
    await update.message.reply_text("🔇 Звук выключен")

async def set_volume(update: Update, context):
    try:
        # Получаем значение громкости, которое пользователь передает
        volume = int(context.args[0])

        # Проверяем, что значение в пределах 0-100
        if 0 <= volume <= 100:
            # Делаем громкость на указанное значение
            Controller.set_volume(volume)
            await update.message.reply_text(f"🔊 Громкость установлена на {volume}%")
        else:
            await update.message.reply_text("❌ Значение громкости должно быть в диапазоне от 0 до 100.")
    except (IndexError, ValueError):
        await update.message.reply_text("❌ Неверный формат команды. Используйте: /setvolume <значение от 0 до 100>.")



def get_handlers():
    return [
        CommandHandler("play", play_pause),
        CommandHandler("next", next_track),
        CommandHandler("prev", prev_track),
        CommandHandler("volup", volume_up),
        CommandHandler("voldown", volume_down),
        CommandHandler("mute", mute),
        CommandHandler("setvolume", set_volume),
    ]
