from django.db import models


class App(models.Model):
    """
    A simple model for an abstract 'application'
    """
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100, unique=True)
