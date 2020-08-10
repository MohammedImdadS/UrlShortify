from django.test import TestCase
from .forms import UserRegisterForm

# Create your tests here.
class TestAccountForm(TestCase):
	def test_register(self):
		form = UserRegisterForm({
			'user': 'imdad',
			'email': 'imdad@ex.com',
			'password1': 'h3!!oPass',
			'password2': 'h3!!oPass',
			})
		self.assertTrue(form.is_valid())

	def test_register_poor_password(self):
		form = UserRegisterForm({
			'user': 'imdad',
			'email': 'imdad@ex.com',
			'password1': 'password',
			'password2': 'password',
			})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['password2'],["This password is too common."])


	def test_register_different_password(self):
		form = UserRegisterForm({
			'user': 'imdad',
			'email': 'imdad@ex.com',
			'password1': 'h3!!oPass',
			'password2': 'h3!!oPas',
			})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['password2'],["The two password fields didn't match."])

	def test_register_bad_email(self):
		form = UserRegisterForm({
			'user': 'imdad',
			'email': 'imdad.com',
			'password1': 'h3!!oPass',
			'password2': 'h3!!oPass',
			})
		self.assertFalse(form.is_valid())
		self.assertEqual(form.errors['email'],["Enter a valid email address."])

