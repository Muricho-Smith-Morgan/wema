from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Help
from django.db import models



class SignUpForm(UserCreationForm):
    class Meta:
      model = User
      fields = ('username', 'password1', 'password2')


class EditForm(forms.ModelForm):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    help_offered = models.CharField(max_length=30)
    
    
    
    class Meta:
        model = Help
        fields = '__all__'

class EditCaseInfoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}))
    help_offered = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
     
    class Meta:
        model = Help
        fields = '__all__'