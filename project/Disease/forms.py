from django import forms

from .models import Disease


class DiseaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
        self.fields['disease_code'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['pathogen'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['id'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Disease
        fields = '__all__'
