from django import forms
from . models import *


class MovieDateForm(forms.ModelForm):

    class Meta:
        model = MovieDate
        exclude = [""]
