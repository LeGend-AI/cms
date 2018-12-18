from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  repeat_password = forms.CharField(widget=forms.PasswordInput)
  # Here we add the extra form fields that we will use to create another model object
  organization = forms.CharField(required=False)
  title = forms.CharField(required=False)

  class Meta:
    model = User
    fields = [ 'username', 'first_name', 'last_name', 'email', 'password', ]
