from telegram import (
    ReplyKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

async def start(update, context):
    buttons = [
            ["Помощь", "Общежитие"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Привет, я помогу тебе с поступлением в СибАДИ.",
            reply_markup=keyboard
    )

async def show_contacts(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="<Вставить сюда контактные данные приёмной комиссии>"
    )

async def show_dormitory_info(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="<Вставить сюда информацию об общежитии>"
    )


async def unknown(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Извините, не могу ответить на этот вопрос."
    )

def main():
    with open('token.txt') as f:
        token = f.readline()[:-1] # remove \n

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(
            filters.Regex("^Помощь$"), show_contacts))

    application.add_handler(MessageHandler(
            filters.Regex("^Общежитие$"), show_dormitory_info))

    application.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    application.run_polling()

if __name__ == '__main__':
    main()

