from django import forms
from .models import Degree, requiredCourses, degreeSpecific


class SearchForm(forms.Form): 
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=(("degree name", "Degree Name"), ("major code", "Major Code")))
class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = "__all__"