from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Departamento, Extra

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['numero', 'metros_2', 'extras']
        widgets = {
            'extras': forms.CheckboxSelectMultiple
        }

class DepartamentoEditForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['extras']
        widgets = {
            'extras': forms.CheckboxSelectMultiple
        }

class ExtraForm(forms.ModelForm):
    class Meta:
        model = Extra
        fields = ['nombre', 'porcentaje']
        widgets = {
            'porcentaje': forms.NumberInput(attrs={'step': '0.01'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']