from django import forms
from .models import Facture, Categorie, Client

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'date_emission', 'montant', 'categorie', 'est_payee']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'email', 'telephone']


