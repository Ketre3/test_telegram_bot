from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from image import image_and_face
from voice import voice_save
from settings import BOT_TOKEN, FILES_FOLDER, USE_TOR_SOCKS


def start(update, context):
    message = update['message']
    uid = message.from_user['id']

    user_folder = FILES_FOLDER / str(uid)
    if not user_folder.exists():
        user_folder.mkdir()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Hello, {uid}!",
    )


def main():
    TOR_SOCKS = {'proxy_url': 'socks5h://127.0.0.1:9050'}
    updater = Updater(
        token=BOT_TOKEN,
        request_kwargs=TOR_SOCKS if USE_TOR_SOCKS else None,
        use_context=True,
    )
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.voice, voice_save))
    dispatcher.add_handler(MessageHandler(Filters.photo, image_and_face))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
