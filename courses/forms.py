from django import forms
from . models import *


class CourseDateForm(forms.ModelForm):

    class Meta:
        model = CourseDate
        exclude = [""]
