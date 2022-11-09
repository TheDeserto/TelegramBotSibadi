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
            ["Приёмная комиссия"],
            ["Помощь", "Общежитие"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    if context.user_data.get("not first launch") == True:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Возвращение в начало.",
                reply_markup=keyboard
        )
    else:
        await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Привет, я помогу тебе с поступлением в СибАДИ.",
                reply_markup=keyboard
        )

    context.user_data["not first launch"] = True

async def show_contacts(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
"""Омск, проспект Мира, д. 5, каб. 1.139
Телефон +7(3812)65-99-88
Email: priem_kom@sibadi.org
Мессенджеры +79131499459
""")
    )

async def show_dormitory_info(update, context):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="<Вставить сюда информацию об общежитии>"
    )

async def show_admiration_committee_info(update, context):
    buttons = [
        ["Необходимые документы"],
        ["Подача", "Сроки приёма"],
        ["В начало"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Какую информацию показать?",
            reply_markup=keyboard
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

    application.add_handler(MessageHandler(
            filters.Regex("^Приёмная комиссия$"), show_admiration_committee_info))

    application.add_handler(MessageHandler(
            filters.Regex("^В начало$"), start))

    application.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    application.run_polling()

if __name__ == '__main__':
    main()

