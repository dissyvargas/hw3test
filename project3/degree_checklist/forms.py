from django import forms
from .models import Degree, requiredCourses, degreeSpecific


#used to search for classes 
class SearchForm(forms.Form): 
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=(("degree name", "Degree Name"), ("subject_name", "Subject Name")))


class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = "__all__"

#variables 
RADIO_CHOICES = (
    ("Value One", "Value One Display"), 
    ("Value Two", "Value Two Display"),
    ("Value Three", "Value Three Display")
)

#example form created to work with forms 
class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES,
                                    widget=forms.RadioSelect)

    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    email_input = forms.EmailField()
    #date_input = forms.DateField(widget=forms.DateInput(attrs="type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

# used to upload forms model form upload 
class UploadForm(forms.Form):
    file_upload = forms.FileField()
