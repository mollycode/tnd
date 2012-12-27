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
        
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

class UserCreationForm(DjangoUserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user