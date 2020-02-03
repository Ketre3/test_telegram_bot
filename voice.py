from settings import FILES_FOLDER
from pydub import AudioSegment


FRAME_RATE = 16 * 1000

def voice_save(update, context):
    message = update['message']
    uid = message.from_user['id']

    voice = message['voice']
    user_folder = FILES_FOLDER / str(uid)

    path_to_oga = _save_voice_file(voice, user_folder)
    path_to_wav = _convert_to_wav(path_to_oga)

    path_to_oga.unlink()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Converted!",
    )
    context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=path_to_wav.open("rb"),
    )

def _save_voice_file(voice, user_folder):
    file = voice.get_file()

    *_, file_name = file.file_path.split('/')
    path_to_save = user_folder / file_name

    file.download(path_to_save)

    return path_to_save

def _convert_to_wav(path_to_oga):
    # oga can easily been opened like ogg file
    ogg = AudioSegment.from_ogg(path_to_oga)
    ogg.set_frame_rate(FRAME_RATE)
    path_to_wav = path_to_oga.parent / (path_to_oga.stem + '.wav')
    ogg.export(path_to_wav, format="wav")
    return path_to_wav
