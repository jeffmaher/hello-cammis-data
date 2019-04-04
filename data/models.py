from django.db import models

class Greeting(models.Model):
    name = models.SlugField(primary_key=True)
    greeting = models.CharField(max_length=200)
    punctuation = models.CharField(max_length=1, default=".")