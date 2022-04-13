from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'biography', 'avatar')



# class UpdateProfileForm(forms.ModelForm):
#     user = OneToOneField(User, on_delete=models.CASCADE)
#     biography = models.TextField(null=False, blank=True)
#     phone = models.CharField(max_length=11)
#     avatar = models.ImageField(upload_to='media/avatars', null=True, blank=True)