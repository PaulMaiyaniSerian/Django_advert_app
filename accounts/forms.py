from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder" : "Username", "autocomplete":"off"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "autocomplete":"off"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder" : "Enter Password", "autocomplete":"off"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Password (repeat)", "autocomplete":"off"}))


    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')
