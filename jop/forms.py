

from django import forms

from .models import Aplly

class Apllyform(forms.ModelForm):
    
    class Meta:
        model = Aplly
        fields = ['name_job', 'email', 'website', 'cv_job', 'cover_letter']

