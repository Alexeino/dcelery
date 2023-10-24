from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import File
from .serializers import FileSerializer
from tasks.tasks import crop_file
from django.conf import settings
# Create your views here.
class UploadFiles(CreateAPIView):
    
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    def post(self, request, *args, **kwargs):

        file = request.data.get("file")
        
        response = super().post(request, *args, **kwargs)
        
        file_path = f"{settings.MEDIA_ROOT}/files/{file.name}".strip()
        print(file_path)
        crop_file.delay(file_path,file.name)
        return response
    
    
class FilesList(ListAPIView):
    queryset= File.objects.all()
    serializer_class = FileSerializer