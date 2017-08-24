from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUsersForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(2000)
        ]
    )