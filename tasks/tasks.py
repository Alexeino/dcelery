from celery import shared_task, current_task
from django.core.mail import send_mail
from PIL import Image
import os
from django.conf import settings

FOLDER = "cropped_files"
OUTPUT_FOLDER_PATH = os.path.join(settings.BASE_DIR, FOLDER)


@shared_task
def crop_file(file_path, filename):
    try:
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        if not os.path.exists(OUTPUT_FOLDER_PATH):
            os.makedirs(OUTPUT_FOLDER_PATH)

        cropped_image_path = os.path.join(OUTPUT_FOLDER_PATH, "thumbnail_" + filename)
        img.save(cropped_image_path)

        current_task.update_state(state="SUCCESS")

        return cropped_image_path

    except FileNotFoundError:
        print(f"File Not Found with Path : ", file_path)
    except Exception as ex:
        print(f"Exception raised : ", ex)


@shared_task
def convert_to_jpg(cropped_image_path):
    try:
        print("Convert to JPG : ", cropped_image_path)

        img = Image.open(cropped_image_path)
        img = img.convert("RGB")
        jpg_image_path = cropped_image_path.replace(".png", ".jpg")
        print("JPG PATH - ", jpg_image_path)
        img.save(jpg_image_path, "JPEG")
        filename = str(jpg_image_path).split("/")[-1]
        print("filename - ", filename)
        jpg_image_url = os.path.join(settings.MEDIA_CROPPED_URL, filename)

        print("JPEG Url - ", jpg_image_url)

        # If task is completed send the email
        send_email(
            subject="Image has been Cropped! Download Now",
            message=f"You image has been cropped and saved. Click here to download http://localhost:8000{jpg_image_url}",
            from_email="admin@test.com",
            recipient_list=["recipent@example.com"],
        )

        return jpg_image_path
    except Exception as ex:
        print(ex)


def send_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
