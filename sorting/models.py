from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalInfo(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=244)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    year_group = models.CharField(max_length=244, null=True, blank=True)
    campus_church = models.CharField(max_length=244, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    missionary = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name