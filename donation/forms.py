from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# `from .models import Account

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Field, Layout


class Amount(forms.Form):
    """ Form for ccepting donation amount in stripe payment """
    CHOICES = [('5', '€5'),
               ('20', '€20'),
               ('50', '€50'),
               ('100', '€100')]

    donate_value = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'btn-check'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Donate', css_class='donate-btn'))
        self.helper.form_method = 'POST'
