from django.db import models
from django.contrib import get_user_model

class Snack(models.Snack):
    name = models.CharField(max_length=256)
    purchaser = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    admin = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
