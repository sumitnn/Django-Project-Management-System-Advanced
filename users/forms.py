from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

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
