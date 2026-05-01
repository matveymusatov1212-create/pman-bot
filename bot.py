import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")
WEBAPP_URL = os.environ.get("WEBAPP_URL")

WELCOME_TEXT = (
    "Добро пожаловать!\n\n"
    "Здесь моё портфолио: визуализации, навесы МАФ и жилые пространства.\n\n"
    "Нажми кнопку ниже 👇"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            "🏠  Открыть портфолио",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]]
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot started...")
app.run_polling()
