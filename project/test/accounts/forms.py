from django import forms
from django.forms import ModelForm
from . models import *

class signup_form(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email","autocomplete":"off"}))
    register_number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Register Number","autocomplete":"off"}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Date of Birth","autocomplete":"off"}))
    user_type = forms.ChoiceField(choices=usertype_choice)
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone","autocomplete":"off"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name","autocomplete":"off"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name","autocomplete":"off"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Fullname","autocomplete":"off"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address","autocomplete":"off"}))
    standard = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Standard","autocomplete":"off"}))
    section = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Section","autocomplete":"off"}))
    data_entry_user = forms.BooleanField(required=False)


class login_form(forms.Form):
    
    
        email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email","autocomplete":"off"}))
        phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone","autocomplete":"off"}))

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
            self.fields['phone'].required = True
            
            
