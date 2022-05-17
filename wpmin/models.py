from django.db import models

# Create your models here.

class Url(models.Model):
    url_text = models.URLField()

    def __str__(self):
        return self.url_text