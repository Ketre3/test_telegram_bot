from settings import FILES_FOLDER
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_fontalface_default.xml"
)

def image_and_face(update, context):
    message = update['message']
    uid = message.from_user['id']
    user_folder = FILES_FOLDER / str(uid)

    photos = message['photo']

    for i, photo in enumerate(photos, start=1):

        path_to_image = _save_image(photo, user_folder)

        if has_face(path_to_image):
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Image {i} saved!",
            )
        else:
            path_to_image.unlink()

            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"There\'s no face in image {i}!",
            )


def _save_image(photo, user_folder):
    file = photo.get_file()

    *_, file_name = file.file_path.split('/')

    path_to_save = user_folder / file_name
    file.download(path_to_save)

    return path_to_save


def has_face(path_to_image):
    opencv_image = cv2.imread(path_to_image)
    gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image)
    return len(faces) != 0
