from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension
from django.core.validators import FileExtensionValidator
import os
from image_repository import settings


# Create your models here.
class image(models.Model):
    name = models.CharField(max_length = 200, default="new_image")
    picture = models.ImageField(upload_to="image_folder", null=True, validators=[FileExtensionValidator(['jpg', 'jpeg', 'jpe', 'jif', 'png', 'gif', 'webp', 'tiff', 'tif'], "File type not supported")])
    owner = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT, null=True, blank=True)
    private = models.BooleanField(default=False)
    search = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.picture.url
    def delete(self, *args, **kwargs):
        path_first = os.path.relpath(self.picture.url, '/media')
        print(settings.MEDIA_ROOT)
        print(path_first)
        os.remove(os.path.join(settings.MEDIA_ROOT, path_first))
        super(image, self).delete(*args, **kwargs)
