from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Facture, Categorie, Client
from .forms import FactureForm, CategorieForm, ClientForm
from .forms import SignUpForm
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from django.http import HttpResponse

class FactureListView(LoginRequiredMixin, ListView):
    model = Facture
    template_name = 'factures/liste_factures.html'  
    context_object_name = 'factures'

class FactureDetailView(LoginRequiredMixin, DetailView):
    model = Facture
    template_name = 'factures/afficher_facture.html'
    context_object_name = 'facture'

class FactureCreateView(LoginRequiredMixin, CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/creer_facture.html'
    success_url = reverse_lazy('liste_factures')

class FactureUpdateView(LoginRequiredMixin, UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/modifier_facture.html'
    success_url = reverse_lazy('liste_factures')

class FactureDeleteView(LoginRequiredMixin, DeleteView):
    model = Facture
    template_name = 'factures/supprimer_facture.html'
    success_url = reverse_lazy('liste_factures')

class FacturePDFView(DetailView):
    model = Facture

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=facture_{self.object.numero}.pdf'

        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle('TitleStyle', parent=styles['Title'], alignment=1, fontSize=18, spaceAfter=12)
        
        normal_style = styles['Normal']
        normal_style.leading = 12 

        title = Paragraph(f'Facture #{self.object.numero}', title_style)
        elements.append(title)
        
        info = [
            ['Client', self.object.client.nom],
            ['Date', self.object.date_emission.strftime('%Y-%m-%d')],
            ['Total TTC', f'{self.object.total_ttc()} €'],
        ]

        

        table = Table(info)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        
        elements.append(Spacer(1, 0.5 * inch)) 
        elements.append(table)
    
        doc.build(elements)

        return response

class CustomLoginView(LoginView):
    template_name = '/login.html' 
    redirect_authenticated_user = True
    next_page = reverse_lazy('liste_factures')

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'factures/signup'
    success_url = reverse_lazy('liste_factures')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class FactureCreateView(LoginRequiredMixin, CreateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/creer_facture.html'
    
    def form_valid(self, form):
        client = get_object_or_404(Client, pk=self.kwargs['client_id'])
        form.instance.client = client
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('liste_factures')


class FactureUpdateView(LoginRequiredMixin, UpdateView):
    model = Facture
    form_class = FactureForm
    template_name = 'factures/modifier_facture.html'
    success_url = reverse_lazy('liste_factures')


class FactureDeleteView(LoginRequiredMixin, DeleteView):
    model = Facture
    template_name = 'factures/supprimer_facture.html'
    success_url = reverse_lazy('liste_factures')


class FactureDetailView(LoginRequiredMixin, DetailView):
    model = Facture
    template_name = 'factures/afficher_facture.html'


class FactureListView(LoginRequiredMixin, ListView):
    model = Facture
    template_name = 'factures/liste_factures.html'
    context_object_name = 'factures'

# Client views
class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/creer_client.html'
    success_url = reverse_lazy('liste_clients')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/modifier_client.html'
    success_url = reverse_lazy('liste_clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'clients/supprimer_client.html'
    success_url = reverse_lazy('liste_clients')


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'clients/afficher_client.html'


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/liste_clients.html'
    context_object_name = 'clients'

# Categorie views
class CategorieCreateView(LoginRequiredMixin, CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'categories/creer_categorie.html'
    success_url = reverse_lazy('liste_categories')


class CategorieUpdateView(LoginRequiredMixin, UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'categories/modifier_categorie.html'
    success_url = reverse_lazy('liste_categories')


class CategorieDeleteView(LoginRequiredMixin, DeleteView):
    model = Categorie
    template_name = 'categories/supprimer_categorie.html'
    success_url = reverse_lazy('liste_categories')


class CategorieDetailView(LoginRequiredMixin, DetailView):
    model = Categorie
    template_name = 'categories/afficher_categorie.html'


class CategorieListView(LoginRequiredMixin, ListView):
    model = Categorie
    template_name = 'categories/liste_categories.html'
    context_object_name = 'categories'