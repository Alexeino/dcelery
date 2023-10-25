from django.urls import path
from .views import UploadFiles, FilesList

urlpatterns = [
    path("upload/", UploadFiles.as_view(), name="upload_file"),
    path("all/", FilesList.as_view(), name="show_files"),
]
