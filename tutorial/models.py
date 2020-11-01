from django.db import models

# Create your models here.
class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} Tutorial"
