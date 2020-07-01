from django.db import models

class InfoTable(models.Model):
    name = models.CharField(default='-',max_length=500)
    price = models.IntegerField(default=0)
    phone = models.CharField(default='-',max_length=25)
    approved = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    qm = models.IntegerField(default=0)
    location = models.CharField(default='-',max_length=500)


    def __str__(self):
        return str(self.name)