from django import forms

class TextForm(forms.Form):
	title = forms.CharField(max_length=100, required=False)
	text = forms.CharField(required=True)

class PhotoForm(forms.Form):
	photo = forms.FileField(required=True)
	caption = forms.CharField(required=False)

class VideoForm(forms.Form):
	video = forms.FileField(required=True)
	description = forms.CharField(required=False)

class AudioForm(forms.Form):
	audio = forms.FileField(required=True)
	description = forms.CharField(required=False)

class QuotePost(forms.Form):
	quote = forms.CharField(required=True)
	source = forms.CharField(required=False)

class LinkPost(forms.Form):
	title = forms.CharField(max_length=100, required=False)
	link = forms.URLField(required=True)

class ChatPost(forms.Form):
	title = forms.CharField(max_length=100, required=False)
	chat = forms.CharField(required=True)
