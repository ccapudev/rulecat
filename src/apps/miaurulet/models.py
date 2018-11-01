from django.db import models
from uuid import  uuid4


# Create your models here.
class SpinResult(models.Model):
    uid = models.UUIDField(default=uuid4)
    resultado = models.TextField()
    apuesta = models.IntegerField(default=8)
    user_id = models.IntegerField(null=False)