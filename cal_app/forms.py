from django import forms
from django.forms import ModelForm
from django.forms import fields
from django.forms.fields import Field
from .models import Venue

#create venue form

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__" # or ('name','address','zip_code','phone','email')
        