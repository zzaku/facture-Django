from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Facture, Categorie, Client
from .forms import FactureForm, CategorieForm, ClientForm
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/factures') 
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def creer_facture(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            facture = form.save(commit=False)
            facture.client = client 
            facture.save()
            return redirect('/factures')
    else:
        form = FactureForm()

    return render(request, 'factures/creer_facture.html', {'form': form, 'client': client})

@login_required
def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('liste_factures')
    else:
        form = FactureForm(instance=facture)
    return render(request, 'factures/modifier_facture.html', {'form': form})

@login_required
def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('liste_factures')
    return render(request, 'factures/supprimer_facture.html', {'facture': facture})

@login_required
def afficher_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'factures/afficher_facture.html', {'facture': facture})

@login_required
def liste_factures(request):
    factures = Facture.objects.all()
    return render(request, 'factures/liste_factures.html', {'factures': factures})

@login_required
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'categories/liste_categories.html', {'categories': categories})

@login_required
def afficher_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    return render(request, 'categories/afficher_categorie.html', {'categorie': categorie})

@login_required
def creer_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'categories/creer_categorie.html', {'form': form})

@login_required
def modifier_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'categories/modifier_categorie.html', {'form': form})

@login_required
def supprimer_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'categories/supprimer_categorie.html', {'categorie': categorie})

@login_required
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste_clients.html', {'clients': clients})

@login_required
def afficher_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/afficher_client.html', {'client': client})

@login_required
def creer_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'clients/creer_client.html', {'form': form})

@login_required
def modifier_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/modifier_client.html', {'form': form})

@login_required
def supprimer_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'clients/supprimer_client.html', {'client': client})
