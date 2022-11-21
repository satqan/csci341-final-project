from django import forms

from .models import DiseaseType


class DiseaseTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiseaseTypeForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = DiseaseType
        fields = '__all__'
