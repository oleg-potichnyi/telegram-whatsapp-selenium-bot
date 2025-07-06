from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from selenium_script import run_selenium


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Вітаю! Я телеграм-бот.")


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я бот, що вміє працювати з WhatsApp, Selenium і Telegram.")


async def run(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Запускаю Selenium.")
    try:
        quotes = run_selenium()  # отримуємо список цитат
        message = "Успішно залогінено. Ось ваші цитати:\n\n"
        for i, quote in enumerate(quotes, 1):
            message += f"{i}. {quote}\n"
        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Сталася помилка: {e}")


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("run", run))

    print("✅ Бот запущено. Очікуємо повідомлень...")
    app.run_polling()


if __name__ == '__main__':
    main()
