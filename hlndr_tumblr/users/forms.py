from django import forms

class RegisterForm(forms.Form):
	username = forms.RegexField(regex=r'^[\w.@+-]+$',
								max_length=30,
								label="username",
								error_messages={
									'invalid':"This value may contain only letters, numbers and @/./+/-/_ characters."})
	password1 = forms.CharField()
	password2 = forms.CharField()
	email = forms.EmailField()
	
class LoginForm(forms.Form):
	username = forms.RegexField(regex=r'^[\w.@+-]+$',
								max_length=30,
								label="username",
								error_messages={
									'invalid':"That username doesn't exist"})
	password = forms.CharField()
