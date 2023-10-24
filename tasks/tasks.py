from celery import shared_task
from PIL import Image
import os
from django.conf import settings

FOLDER = "cropped_files"
OUTPUT_FOLDER_PATH = os.path.join(settings.BASE_DIR,FOLDER)

@shared_task
def crop_file(file_path,filename):
    try:
        img = Image.open(file_path)
        print(img)
        print(filename)
        img.thumbnail((200,200))
        if not os.path.exists(OUTPUT_FOLDER_PATH):
            os.makedirs(OUTPUT_FOLDER_PATH)
        img.save(os.path.join(OUTPUT_FOLDER_PATH,"thumbnail_"+filename))
    except FileNotFoundError:
        print(f"File Not Found with Path : ",file_path)
    except Exception as ex:
        print(f"Exception raised : ",ex)