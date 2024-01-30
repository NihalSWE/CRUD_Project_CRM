from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import ClientData

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        # Adding Bootstrap classes for styling
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['placeholder'] = f'Enter {field_name.capitalize()}'

# Login user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(strip=False, widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))


class AddDataForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = ['first_name','last_name','email','phone','address','city','country']


class UpdateDataForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = ['first_name','last_name','email','phone','address','city','country']