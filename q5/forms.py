from django import forms
from .models import series, user, subscription
from django.utils.translation import ugettext_lazy as _

class SubscriptionForm(forms.Form): 
	email = forms.CharField(label='email', max_length=100, widget=forms.TextInput(attrs={'class': "input1", 'placeholder':"Email"}))
	series = forms.CharField(label='series', max_length=100, widget=forms.TextInput(attrs={'class': "input1", 'placeholder':"Name of TV-Series"}))