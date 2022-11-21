from django import forms

from .models import PublicServant


class PublicServantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicServantForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['department'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = PublicServant
        fields = '__all__'
