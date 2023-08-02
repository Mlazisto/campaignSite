from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """
    Custom User Registration Form that extends Django's UserCreationForm.

    :param first_name: CharField representing the first name of the user.
    :type first_name: django.forms.CharField

    :param last_name: CharField representing the last name of the user.
    :type last_name: django.forms.CharField

    :param email: EmailField representing the email address of the user.
    :type email: django.forms.EmailField

    :returns: A form to register a new user with fields for username, first name, last name,
              email, password1, and password2.
    :rtype: django.forms.ModelForm
    """
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        """
        Meta class to define the model and fields for the UserRegistrationForm.

        :param model: User model to use for registration.
        :type model: django.contrib.auth.models.User

        :param fields: List of fields to include in the form.
        :type fields: list
        """
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']