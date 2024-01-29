from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput

from django import forms





# Register user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


# Login user
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'autofocus': True}))
    password = forms.CharField(strip=False, widget=PasswordInput())

