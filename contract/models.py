from django.db import models


class Contract(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

