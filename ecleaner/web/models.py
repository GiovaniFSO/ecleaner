from django.db import models

# Create your models here.

class Cleaner(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=12, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=11, null=False, blank=False)
    street = models.CharField(max_length=60, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    neighborhood = models.CharField(max_length=30, null=False, blank=False)
    complement = models.CharField(max_length=100, null=False, blank=True)
    zip_code = models.CharField(max_length=30, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    code = models.IntegerField(null=False, blank=False)
    profile_picture = models.ImageField(null=False)
