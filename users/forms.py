from django.forms import ModelForm, Textarea

from models import UserProfile

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "age", "sex", "country", "background_field", "desire")
        widgets = {
            'desire': Textarea(attrs={'cols': 80, 'rows': 20}),
        }