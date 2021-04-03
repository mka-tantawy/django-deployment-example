from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserFrom(forms.ModelForm):
    """docstring for UserProfileInfoFrom."""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    """docstring for UserProfileInfoForm."""

    class Meta():
        model = UserProfileInfo
        fields = ('site','profile_pic')
