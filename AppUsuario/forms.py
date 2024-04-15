from django import forms
from .models import Usuario

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username']
    
class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    usuario_administrador = forms.BooleanField(label='¿Quieres que este usuario sea administrador?', required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombres', 'apellidos', 'imagen', 'password','usuario_administrador'] 

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password = make_password(self.cleaned_data["password"])
        usuario.usuario_administrador = self.cleaned_data["usuario_administrador"]
        if commit:
            usuario.save()
        return usuario

class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'nombres', 'apellidos']

    password = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if password and len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if password and not any(char.isupper() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        if password and not any(char.islower() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra minúscula.")

        if password and not any(char.isdigit() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un dígito.")

        return cleaned_data
    
class UsuarioPasswordForm(forms.ModelForm):
    password = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        if password and len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        if password and not any(char.isupper() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")

        if password and not any(char.islower() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra minúscula.")

        if password and not any(char.isdigit() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un dígito.")

        return cleaned_data