from django import forms

from .models import User
from blood_alert.models import BLOOD_TYPES

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'name', 'blood_type', 'phone')
        email = forms.EmailField(label='Enter your email', required=True)
        username = forms.CharField(label='Enter a username', required=True)
        name = forms.CharField(label='Enter your Full Name', required=True)
        password= forms.CharField(label='Enter your Password', widget=forms.PasswordInput(), required=True)
        password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), required=True)
        blood_type = forms.MultipleChoiceField(choices=BLOOD_TYPES, label='Choose your Blood Type', required=True)
        phone = forms.CharField(label='Enter your phone number', required=True)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'blood_type')
        username = forms.CharField(label='Enter your username', required=True)
        password = forms.CharField(label='Enter your password', widget=forms.PasswordInput(), required=True)
        blood_type = forms.MultipleChoiceField(choices=BLOOD_TYPES, label='Choose your Blood Type', required=True)
