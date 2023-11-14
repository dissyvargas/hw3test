from django import forms

RADIO_CHOICES = (
    ("Value One", "Value One Display"), 
    ("Value Two", "Value Two Display"),
    ("Value Three", "Value Three Display")
)
CLASSIFICATION_CHOICES = (
    (
        "Undergraduate", (
            ("1", "Freshman"),
            ("2", "Sophomore"),
            ("3", "Junior"),
            ("4", "Senior")
        )
    ),
    (
        "Graduate", (
            ("1st year"), 
            ("2nd year")
        )
    )
)
class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES,
                                    widget=forms.RadioSelect)
    classification = forms.ChoiceField(choices=CLASSIFICATION_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    email_input = forms.EmailField()
    #date_input = forms.DateField(widget=forms.DateInput(attrs="type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")