from django.forms import ModelForm, Textarea
from django.forms.widgets import TextInput

from models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "age", "sex", "country", "education_level", "background_field", "desire")
        widgets = {
            "age": TextInput(attrs={'size':'1','maxlength':'3'}),
            "desire": Textarea(attrs={'cols': 80, 'rows': 20}),
        }