from django import forms

from .models import Account

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['name', 'email', 'password']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'password': 'Create Password'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False