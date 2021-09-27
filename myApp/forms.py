from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userinfo
from django import forms
from django.db import transaction

class createUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_active = False
        user.save()
        return user

class UserinfoForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ['full_Name', 'phone', 'state', 'address']