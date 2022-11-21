from django import forms

from .models import Record


class RecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['disease_code'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['total_deaths'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '0'
        }
        self.fields['total_patients'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '0'
        }

    class Meta:
        model = Record
        fields = '__all__'
