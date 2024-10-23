from django.urls import path
from . import views
from .views import (
    FactureCreateView, FactureUpdateView, FactureDeleteView, FactureDetailView, FactureListView,
    ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView, ClientListView,
    CategorieCreateView, CategorieUpdateView, CategorieDeleteView, CategorieDetailView, CategorieListView
)

urlpatterns = [
    path('modifier/<int:pk>/', FactureUpdateView.as_view(), name='modifier_facture'),
    path('supprimer/<int:pk>/', FactureDeleteView.as_view(), name='supprimer_facture'),
    path('afficher/<int:pk>/', FactureDetailView.as_view(), name='afficher_facture'),
    path('<int:pk>/pdf/', FactureDetailView.as_view(), name='pdf_facture'),
    path('', FactureListView.as_view(), name='liste_factures'),
    path('clients/<int:client_id>/creer_facture/', FactureCreateView.as_view(), name='creer_facture'),

    path('categories/', CategorieListView.as_view(), name='liste_categories'),
    path('categories/afficher/<int:pk>/', CategorieDetailView.as_view(), name='afficher_categorie'),
    path('categories/creer/', CategorieCreateView.as_view(), name='creer_categorie'),
    path('categories/modifier/<int:pk>/', CategorieUpdateView.as_view(), name='modifier_categorie'),
    path('categories/supprimer/<int:pk>/', CategorieDeleteView.as_view(), name='supprimer_categorie'),

    path('clients/', ClientListView.as_view(), name='liste_clients'),
    path('clients/afficher/<int:pk>/', ClientDetailView.as_view(), name='afficher_client'),
    path('clients/creer/', ClientCreateView.as_view(), name='creer_client'),
    path('clients/modifier/<int:pk>/', ClientUpdateView.as_view(), name='modifier_client'),
    path('clients/supprimer/<int:pk>/', ClientDeleteView.as_view(), name='supprimer_client'),
]
