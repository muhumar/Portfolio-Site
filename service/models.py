from django.db import models

# Create your models here.

class Service(models.Model):
    niche = models.CharField(max_length=120)
    service1 = models.CharField(max_length=120)
    service2 = models.CharField(max_length=120)
    service3 = models.CharField(max_length=120)

    def __str__(self):
        return str(self.id)
