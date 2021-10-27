from django import forms
from crispy_forms.helper import FormHelper

from .models import Donation

# `from .models import Account

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Field, Layout


class Amount(forms.ModelForm):

    amount = forms.DecimalField(min_value=5, max_value=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'

        placeholders = {
            'amount': '€5 - €100'
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    class Meta():
        model = Donation
        fields = ['amount']
