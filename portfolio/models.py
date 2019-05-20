from django.db import models

# Create your models here.


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Portfolio(models.Model):
    niche = models.CharField(max_length=120,null=True,blank=True)
    title = models.CharField(max_length=120,null=True,blank=True)
    Description = models.TextField()
    project_link = models.CharField(max_length=120)
    Image = models.ImageField(upload_to=upload_location,blank=True,null=True)

    def __str__(self):
        return str(self.id)
