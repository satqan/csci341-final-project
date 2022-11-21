from django import forms

from .models import Country


class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['cname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['population'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }

    class Meta:
        model = Country
        fields = '__all__'
