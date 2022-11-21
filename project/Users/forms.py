from django import forms

from .models import Users


class UsersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsersForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['surname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['salary'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        self.fields['phone'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        self.fields['cname'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Users
        fields = '__all__'
