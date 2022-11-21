from django import forms

from .models import Specialize


class SpecializeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpecializeForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Specialize
        fields = '__all__'
