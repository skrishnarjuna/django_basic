from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class newuser(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.BigIntegerField(default=NULL)
    email = models.EmailField(max_length=50)

    class Meta:
        db_table = 'user_details'