from django import forms
from web_basics_exam.web_basics_exam.main_app.models.profile import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileForm(ProfileForm):
    pass
