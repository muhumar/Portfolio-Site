from django.db import models

# Create your models here.


class Profile(models.Model):
    email = models.EmailField()
    address = models.CharField(max_length=120, null=True, blank=True)
    contact_no = models.CharField(max_length=20, null=True, blank=True)
    overview = models.TextField()
    website = models.CharField(max_length=320, null=True, blank=True)
    twitter = models.CharField(max_length=120, null=True, blank=True)
    instagram = models.CharField(max_length=120, null=True, blank=True)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    linkedIn = models.CharField(max_length=120, null=True, blank=True)
    image1 = models.ImageField()
    image2 = models.ImageField()

    def __str__(self):
        return str(self.email)
