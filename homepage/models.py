from django.db import models

# Create your models here.
SUBSCRIBE_STATUS = (
    (0, "not_subscribed"),
    (1,"subscribed"),
)
class Contact(models.Model):
    name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=100)
    phone =  models.IntegerField()
    time =  models.CharField(max_length=200)
    comments =  models.TextField()

    def __str__(self):
        return f'message from {self.name}'
class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    subscribe_status = models.IntegerField(choices=SUBSCRIBE_STATUS, default=0)
    def __str__(self):
        return f'{self.email} subscribed'