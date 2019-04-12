from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    
    class Meta:
        model = UserInfo
        fields = ("phone_number",)

