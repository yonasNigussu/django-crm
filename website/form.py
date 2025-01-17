from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email address'}))
    first_name= forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name= forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))


    class Meta:
        model= User
        field=('username','first_name','last_name','password1','password2')

