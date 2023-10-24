from celery import shared_task, current_task
from django.core.mail import send_mail
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
        
        # If task is completed send the email
        send_email(
            subject="Image has been Cropped",
            message="You image has been cropped and saved.",
            from_email="admin@test.com",
            recipient_list=["recipent@example.com"]
        )
        
        current_task.update_state(state="SUCCESS")
        

    except FileNotFoundError:
        print(f"File Not Found with Path : ",file_path)
    except Exception as ex:
        print(f"Exception raised : ",ex)
        
def send_email(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)