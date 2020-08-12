from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order # Tells us which model this form is built for
        fields = '__all__' # Saying that create a form with all of Order Models fields otherwise use a list ['']
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']