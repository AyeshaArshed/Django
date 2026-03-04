import re

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    phone_no = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder':'Phone (optional)'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        if password:
            if len(password) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long")
            if not re.search(r"[A-Z]", password):
                raise forms.ValidationError("Password must contain at least one uppercase letter")
            if not re.search(r"[a-z]", password):
                raise forms.ValidationError("Password must contain at least one lowercase letter")
            if not re.search(r"[0-9]", password):
                raise forms.ValidationError("Password must contain at least one number")
            if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
                raise forms.ValidationError("Password must contain at least one special character")
            return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))