from django.core.exceptions import ValidationError
import os
'''
#check if the uploaded file is an image or not
#limited file extensions supported
def validate_extension(value):
    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.jpe', '.jif', '.png', '.gif', '.webp', '.tiff', '.tif']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Only images supported')
'''
def check_validation_error(request, new_image):
    try:
        new_image.full_clean()
    except ValidationError as e:
        picture_error = e.message_dict.get('picture')
        for msg in picture_error:
            messages.error(request, f"{msg}")
    else:
        new_image.save()
