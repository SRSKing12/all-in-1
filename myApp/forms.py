from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userinfo
from django import forms
from django.db import transaction

class createUserForm(UserCreationForm):
    email = forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='UserName',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.TextInput(attrs={'class':'form-control'}),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_active = False
        user.save()
        return user

class UserinfoForm(forms.ModelForm):
    full_Name=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Userinfo
        fields = ['full_Name', 'phone', 'state', 'address']
        widgets={
            'full_Name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }
