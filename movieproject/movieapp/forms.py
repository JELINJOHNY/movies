from .  models import  Movie
from django import forms

class MOVIEForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','description','year','img']