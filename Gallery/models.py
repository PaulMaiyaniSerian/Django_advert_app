from django.db import models

# Create your models here.
class Gallery(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"picture for {self.title}"

class OtherGallery(models.Model):
    picture = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"picture for {self.title}"