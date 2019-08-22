from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)


    def __str__(self):
        return "%s" % (self.title)


