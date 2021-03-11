from django.db import models

# Create your models here.
class ImageModel(models.Model):
    ACTIVITY_TYPES = (
        ('NATURE', 'nature'),
        ('FESTIVALS', 'festivals'),
        ('TRAVEL', 'travel'),
        ('CELEBRATION', 'celebration'),
    )
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=ACTIVITY_TYPES)

