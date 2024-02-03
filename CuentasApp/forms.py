from django import forms
from django.contrib.auth.forms import UserChangeForm 
from django.contrib.auth.models import User

class FormularioEdicionUsuario(UserChangeForm):
    # email = forms.EmailField(lael="Modificar E-mail")
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(),required=False
    )

    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget = forms.PasswordInput) 
    class Meta:
        model = User 
        fields = ['email', 'first_name', 'last_name', 'password1','password2']

    def clean_password2(self):
        print(self.cleaned_data)

        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

