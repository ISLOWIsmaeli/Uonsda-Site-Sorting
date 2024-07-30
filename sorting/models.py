from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=244)
    gender = models.CharField(max_length=244)
    year_group = models.CharField(max_length=244)
    campus_church = models.CharField(max_length=244)