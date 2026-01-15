
from django import forms

class connectForm(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
