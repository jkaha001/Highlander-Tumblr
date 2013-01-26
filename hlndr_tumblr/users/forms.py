from django import forms

class RegisterForm(forms.Form):
	registerUsername = forms.CharField(max_length=30)
	registerPassword = forms.CharField(max_length=200)
	reEnterPassword = forms.CharField(max_length=200)
	registerEmail = forms.CharField(max_length=200)
	
class LoginForm(forms.Form):
	username = forms.CharField(max_length=30)
	password = forms.CharField(max_length=200)	
