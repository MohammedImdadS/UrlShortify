from django.contrib.auth.models import User
from django.db import models
import random
import string
# Create your models here.
class Urltab(models.Model):
	longurl  = models.CharField(max_length = 250)
	shorturl = models.CharField(max_length = 7)

	def __str__(self):
		return f"Longurl is - {self.longurl} and its shorturl is - {self.shorturl} "

	def save(self,*args,**kwargs):
		if self.shorturl is None or self.shorturl == '':
			self.shorturl = shorturl_check()
		if not 'http' in self.longurl:
			self.longurl = 'http' + self.longurl
		super(Urltab, self).save(*args,**kwargs)

def shorturl_gen():
	size = 7
	alpha_digits = string.ascii_lowercase + string.digits
	new_url = ''
	for _ in range(size):
		new_url += random.choice(alpha_digits)
	return new_url

def shorturl_check():
	new_url = shorturl_gen()
	data_exist = Urltab.objects.filter(longurl = new_url).exists()
	if data_exist:
		return shorturl_check()
	return new_url


class User_account(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	url =models.ManyToManyField(Urltab, related_name = "user_url")
	
	def __str__(self):
		return f"user -- {self.user}"