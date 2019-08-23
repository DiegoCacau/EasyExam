from django.db import models


class Config(models.Model):

    key = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.key + ': ' + self.value

    def get(key):
        c = Config.objects.get(key=key)
        return c.value
