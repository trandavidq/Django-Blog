from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class blog_post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    body = models.TextField()
