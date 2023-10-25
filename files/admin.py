from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import File

# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ["file", "uploaded_at"]

    class Meta:
        model = File


admin.site.register(File, FileAdmin)
