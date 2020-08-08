from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Urltab

class Urlform(forms.ModelForm):
	class Meta:
		model   = Urltab
		fields  = ['longurl',]
		widgets = {'longurl':forms.TextInput(attrs={' placeholder ': "Long url" })}
		
		
