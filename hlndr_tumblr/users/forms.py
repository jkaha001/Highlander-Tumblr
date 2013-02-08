from django import forms

class RegisterForm(forms.Form):
	GENDER_CHOICES = ( ('u', 'Undisclosed'), ('m', 'Male'), ('f', 'Female') )


	username = forms.RegexField(regex=r'^[\w.@+-]+$',
								max_length=30,
								label="username",
								error_messages={
								'invalid':"This value may contain only letters, numbers and @/./+/-/_ characters."})
	password1 = forms.CharField()
	password2 = forms.CharField()
	email = forms.EmailField()
	birthday = forms.DateField()
	nickname = forms.CharField(required=False)
	gender = forms.ChoiceField(choices=GENDER_CHOICES)
	interests = forms.CharField(max_length=300, required=False)
	
	
class LoginForm(forms.Form):
	username = forms.RegexField(regex=r'^[\w.@+-]+$',
								max_length=30,
								label="username",
								error_messages={
									'invalid':"That username doesn't exist"})
	password = forms.CharField()
