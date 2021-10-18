from django import forms
from models import BlogPosts
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from animals.widgets import CustomClearableFileInput


class blogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        placeholders = {
            'title': 'Blog title',
            'author': 'author',
            'story': 'Blog content',
            'image': 'Upload image',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    class Meta:
        model = BlogPosts()
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)