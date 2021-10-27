from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """ Mofel form form for contactform """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-black'))
        self.helper.form_method = 'POST'

        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'question': 'How can we help?'
        }

        # self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'question']