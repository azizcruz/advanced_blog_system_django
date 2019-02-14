from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_images/default.png', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    # Resizing big images dimensions.
    def save(self, *args, **kwargs):
        '''Overriding Save Method To Resize Image After Creating A Profile'''
        try:
            # EXECUTE THE ORIGINAL SAVE METHOD FIRST.
            super().save(*args, **kwargs)

            # GET THE IMAGE.
            img = Image.open(self.image.path)

            if img.height > 300 and img.width > 300:
                # NEW SIZE.
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            print("Error Occured")
        
        

