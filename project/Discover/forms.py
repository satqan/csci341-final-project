from django import forms

from .models import Discover


class DiscoverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DiscoverForm, self).__init__(*args, **kwargs)
        self.fields['cname'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['disease_code'].widget.attrs = {
            'class': 'form-control col-md-6',
        }
        self.fields['first_enc_date'].widget = forms.DateInput(
            attrs={
                'class': 'form-control col-md-6',
                'type': 'date',
            }
        )

    class Meta:
        model = Discover
        fields = '__all__'
