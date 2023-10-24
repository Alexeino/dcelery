from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import File
from .serializers import FileSerializer

# Create your views here.
class UploadFiles(CreateAPIView):
    
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    
class FilesList(ListAPIView):
    queryset= File.objects.all()
    serializer_class = FileSerializer