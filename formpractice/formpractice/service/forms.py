from.models import form
from django import forms

class contactform(forms.ModelForm):
    class Meta :
        model=form
        fields = [
            'name','email','phone',
        ]