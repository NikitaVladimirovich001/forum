from django import forms
from forum_profile.models import Profile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['id']