import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

TOKEN = os.environ.get("TOKEN")

ORDER_CONTACT = """
📦 For Product Orders

Please Contact:

Shekhar Gubbi
HEXADOX Field Staff

☎ 9886090953
"""


async def show_menu(update: Update):

    keyboard = [
        [
            InlineKeyboardButton(
                "🟣 Trichology Range",
                callback_data="Trichology"
            )
        ],
        [
            InlineKeyboardButton(
                "🟠 Cosmetology Range",
                callback_data="Cosmetology"
            )
        ],
        [
            InlineKeyboardButton(
                "🔵 Clinical Dermatology Range",
                callback_data="Clinical_Dermatology"
            )
        ]
    ]

    await update.message.reply_text(
        "Welcome Doctor 👨‍⚕️\n\n"
        "HEXADOX Dermatology Portfolio\n\n"
        "Please select Product Range:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.upper() == "HEXADOX":
        await show_menu(update)


async def send_images(update: Update, folder):

    query = update.callback_query
    await query.answer()

    path = f"products/{folder}"

    if not os.path.exists(path):
        await query.message.reply_text(
            "Products will be added soon."
        )
        return

    for image in sorted(os.listdir(path)):

        if image.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):

            with open(
                os.path.join(path, image),
                "rb"
            ) as photo:

                await query.message.reply_photo(
                    photo=photo
                )

    await query.message.reply_text(
        ORDER_CONTACT
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await send_images(
        update,
        query.data
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT,
        text_handler
    )
)

app.add_handler(
    CallbackQueryHandler(button_handler)
)


print("HEXADOX Bot Running")

app.run_polling()
