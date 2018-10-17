from django import forms
from .models import series, user, subscription
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form): 
	email = forms.CharField(id='email', max_length=100)
	series = forms.CharField(id='series', max_length=100)