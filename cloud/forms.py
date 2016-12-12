from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Uploads

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'autocomplete': False}))

    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'autocomplete': False}))


class SignUpForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, 
								widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'required':True}))

    password = forms.CharField(label="Password", max_length=30, min_length=8,
    							widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'required':True}))
    rep_password = forms.CharField(label="Password (again)", max_length=30, min_length=8,
    							widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'rep_password', 'required':True}))

    first_name = forms.CharField(label="First Name", max_length=30,
    							widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'fname'}))

    last_name = forms.CharField(label="Last Name", max_length=30,
    							widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lname'}))