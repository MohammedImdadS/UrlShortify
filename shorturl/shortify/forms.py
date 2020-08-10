# from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Urltab
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Urlform(forms.ModelForm):
	class Meta:
		model   = Urltab
		fields  = ['longurl',]
		widgets = {'longurl':forms.TextInput(attrs={' placeholder ': "Long url" })}
		
		
class UserRegisterForm(UserCreationForm):
	class Meta:
		model  = User
		fields = ['username','email','password1','password2']
		