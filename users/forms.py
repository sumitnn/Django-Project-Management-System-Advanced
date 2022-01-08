from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Project
from django.forms import *
User = get_user_model()


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = field.label

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'current_time']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'team_members': TextInput(attrs={'class': 'form-control'}),
            'project_img': FileInput(attrs={'class': 'form-control'}),
            'project_type': TextInput(attrs={'class': 'form-control'}),
            'notes': TextInput(attrs={'class': 'form-control'}),
            'project_file': FileInput(attrs={'class': 'form-control'}),
            'description': TextInput(attrs={'class': 'form-control'}),
        }
