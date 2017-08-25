from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUsersForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(2000)
        ]
    )


class SendMailForm(forms.Form):
    to = forms.EmailField(label='TO', max_length=200)
    subject = forms.CharField(label='SUBJECT', max_length=200)
    body = forms.CharField(label='BODY', widget=forms.Textarea)