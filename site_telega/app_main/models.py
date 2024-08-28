from django.db import models


class ShapeRetention(models.Model):
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    task = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Заявки"