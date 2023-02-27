from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from application.models import Client

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required = True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label='password',strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class ClientForm(forms.ModelForm):
     class Meta:
         model = Client
         fields = ['client_name']
