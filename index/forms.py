from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets   
from .models import *

class keep_me_interested_form(ModelForm):
    class Meta:
        model = keep_me_interested
        fields = ["name", "phone_number", "email"]

class enquiry_form(ModelForm):
    class Meta:
        model = enquiry
        fields = ["name", "phone_number", "email","message"]

class plan_a_visit_form(ModelForm):
    class Meta:
        model = plan_a_visit
        fields = ["name", "phone_number", "email","preferred_time","preferred_date"]
        widgets = {
            "preferred_date" : forms.TextInput(attrs={'type': 'date'}),
            "preferred_time" : forms.TextInput(attrs={'type': 'time'})
        }

