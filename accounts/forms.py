from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order # Tells us which model this form is built for
        fields = '__all__' # Saying that create a form with all of Order Models fields otherwise use a list ['']
        
