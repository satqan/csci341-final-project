from django import forms

from .models import Doctor


class DoctorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['degree'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Doctor
        fields = '__all__'
