from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=200,blank=True)
    content = models.CharField(max_length=200,blank=True)
