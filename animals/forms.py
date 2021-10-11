from django import forms
from home.models import Animal
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .widgets import CustomClearableFileInput


class addAnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        placeholders = {
            'name': 'full_name(in this format)',
            'friendly_name': 'First Name',
            'type': 'Type of animal(e.g Dog, cat...)',
            'breed': 'Breed of animal?',
            'about': 'About the animal',
            'image': 'Image'
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    class Meta:
        model = Animal
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
