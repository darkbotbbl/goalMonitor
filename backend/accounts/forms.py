from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()

# custom user creation form
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email", )