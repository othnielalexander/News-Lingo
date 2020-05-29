from django import forms

class NewsForm(forms.Form):
    news = forms.CharField(label='Enter News for verification')
    