from django import forms

from python_web_basics_exam.profile_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
