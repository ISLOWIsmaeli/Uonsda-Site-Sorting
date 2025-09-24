from django import forms
from . import models

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = models.PersonalInfo
        fields = ['name', 'gender', 'year_group', 'campus_church']

class ExcelUploadForm(forms.Form):
    file=forms.FileField(label='Select Excel File')