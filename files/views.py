from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import File
from .serializers import FileSerializer
from tasks.tasks import crop_file, convert_to_jpg
from django.conf import settings
from celery import chain


# Create your views here.
class UploadFiles(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        file = request.data.get("file")

        response = super().post(request, *args, **kwargs)

        file_path = f"{settings.MEDIA_ROOT}/files/{file.name}".strip()
        
        # Chaining multiple tasks using .s() | operators
        processing_chain = crop_file.s(file_path, file.name) | convert_to_jpg.s()
        processing_chain.apply_async()
        # crop_file.delay(file_path,file.name)
        return response


class FilesList(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
