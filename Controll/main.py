from telegram.ext import Application
from bot import get_handlers
import os
from dotenv import load_dotenv

# Загружаем токен бота
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    for handler in get_handlers():
        app.add_handler(handler)

    print("🎶 Бот запущен! Управление громкостью работает.")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
