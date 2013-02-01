from django import forms

class PostForm(ModelForm):
	title = forms.CharField(max_length=100)
	text = forms.TextField()
	tags = forms.TextField(required=False)
