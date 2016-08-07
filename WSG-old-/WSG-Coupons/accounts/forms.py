from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from .models import Person

class PersonCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(PersonCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = Person
        fields = ("username","first_name","last_name","date_of_birth","phone_number","email","password1","password2",)

class PersonChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(PersonChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = Person
        fields = '__all__'
    

    
    
