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
        ["Образовательные программы"],
        ["Приёмная комиссия"],
        ["Помощь", "Общежитие"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    if context.user_data.get("not first launch"):
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

async def training_programs(update, context):
    buttons = [
        ["Бакалавриат"],
        ["Специалитет"],
        ["Магистратура"],
        ["Аспирантура"],
        ["В начало"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите программу подготовки:",
        reply_markup=keyboard
    )

async def bachelor(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Программы подготовки Бакаравриат: https://sibadi.org/student/educational-programs/bachelor/"
    )

async def speciality(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Программы подготовки Специалитет: https://sibadi.org/student/educational-programs/speciality/"
    )

async def master(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Программы подготовки Магистратура: https://sibadi.org/student/educational-programs/master/"
    )

async def graduate(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Программы подготовки Аспирантура: https://sibadi.org/student/educational-programs/graduate/"
    )
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
        text="https://sibadi.org/entrant/hostel/?ysclid=las86yprkt78081357"
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


async def document_feeding(update, context):
    buttons = [
        ["Подача документов онлайн"],
        ["Подача почтой России", "Подача документов лично"],
        ["В начало"]
    ]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите способ подачи документов",
        reply_markup=keyboard
    )


async def submission_online(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Инструкция для подачи онлайн: https://sibadi.org/abitur2021/lp/instruktsiyaonlayn/"
    )


async def send_mail(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Для подачи документов Почтой России отправьте копии "
             "документов об образовании, документы удостоверяющие личность заказным письмом и"
             "необходимые заявления по адресу 644080, Омская область, г. Омск, Пр. Мира 5, каб. 1.139"
    )


async def give_person(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Подать документы на поступление можно лично по адресу г. Омск, "
             "пр. Мира 5, главный корпус, каб. 1.139, пн-птн с 9:00 до 16:00, сб.10:00 - 13.00"
    )

async def calendar(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="https://sibadi.org/abitur2021/lp/kalendarabiturienta/?ysclid=las9nfbavt528044682"
    )

async def required_documents(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="https://sibadi.org/entrant/commission/priemnaya-komissiya-2023/?ysclid=las8icfb3b36269298"
    )


###
#
async def unknown(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Извините, не могу ответить на этот вопрос."
    )


def main():
    with open('token.txt') as f:
        token = f.readline()[:-1]  # remove \n

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(
        filters.Regex("^Помощь$"), show_contacts))

    application.add_handler(MessageHandler(
        filters.Regex("^Общежитие$"), show_dormitory_info))

    application.add_handler(MessageHandler(
        filters.Regex("^Необходимые документы$"), required_documents))

    application.add_handler(MessageHandler(
        filters.Regex("^Образовательные программы$"), training_programs))

    application.add_handler(MessageHandler(
        filters.Regex("^Бакалавриат$"), bachelor))

    application.add_handler(MessageHandler(
        filters.Regex("^Специалитет$"), speciality))

    application.add_handler(MessageHandler(
        filters.Regex("^Магистратура$"), master))

    application.add_handler(MessageHandler(
        filters.Regex("^Аспирантура$"), graduate))

    application.add_handler(MessageHandler(
        filters.Regex("^Подача$"), document_feeding))

    application.add_handler(MessageHandler(
        filters.Regex("^Подача документов онлайн$"), submission_online))

    application.add_handler(MessageHandler(
        filters.Regex("^Подача почтой России$"), send_mail))

    application.add_handler(MessageHandler(
        filters.Regex("^Подача документов лично$"), give_person))

    application.add_handler(MessageHandler(
        filters.Regex("^Приёмная комиссия$"), show_admiration_committee_info))

    application.add_handler(MessageHandler(
        filters.Regex("^Сроки приёма$"), calendar))

    application.add_handler(MessageHandler(
        filters.Regex("^В начало$"), start))

    application.add_handler(MessageHandler(filters.COMMAND | filters.TEXT, unknown))

    application.run_polling(stop_signals=None)


if __name__ == '__main__':
    main()
