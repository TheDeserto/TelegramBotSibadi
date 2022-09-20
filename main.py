from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters
)

async def start(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Привет, я помогу тебе с поступлением в СибАДИ."
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
    application.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    application.run_polling()

if __name__ == '__main__':
    main()

