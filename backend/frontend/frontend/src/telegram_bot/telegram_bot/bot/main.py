import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import start, help_command, appointments, notifications
from bot.config import BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрация handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("appointments", appointments))
    
    application.run_polling(allowed_updates=[])

if __name__ == "__main__":
    main()