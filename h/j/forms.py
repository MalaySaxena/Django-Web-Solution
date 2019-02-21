from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name needs start with z")


class formname(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    vmail = forms.EmailField(label='enter again')
    text = forms.CharField()


    def clean(self):
        all_data = super().clean()
        email = all_data['email']
        vmail = all_data['vmail']

        if email != vmail:
            raise forms.ValidationError("match it")
