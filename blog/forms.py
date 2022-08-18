from dataclasses import field
from pyexpat import model
from turtle import hideturtle
from django import forms
from django.contrib.auth.forms import  UserChangeForm
from django.contrib.auth.models import User

from .models import Avatar

class clienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    vehiculo = forms.CharField()

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget =forms.HiddenInput(), required= False
    )

    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if (password2 != self.cleaned_data["password1"]):
            raise forms.ValidationError("las contraseñas no coinciden")

        return password2

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)


    