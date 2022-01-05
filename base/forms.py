from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):

    username = UsernameField(widget = forms.TextInput(attrs = {
        'class':'username','placeholder': "username",'id':'id_username',"onkeypress":"return /[a-z]/i.test(event.key)"
    }))

    password = forms.CharField(widget= forms.PasswordInput(attrs = {
        'class':'password-class','placeholder': 'please enter password'
    }))



class RegisterUser(UserCreationForm):
    
    username = forms.CharField(widget = forms.TextInput(attrs = {
        'class':'username','placeholder': "username",'id':'id_username',"onkeypress":"return /[a-z]/i.test(event.key)"
    }))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class': 'password','placeholder':'password'
    }))
    
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class':'password1','placeholder':'Enter password Again','id':'id_password2'
    }))


    class Meta:
        model = User
        fields =['username','password1','password2']