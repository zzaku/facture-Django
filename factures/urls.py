from django.urls import path
from . import views

urlpatterns = [
    path('modifier/<int:pk>/', views.modifier_facture, name='modifier_facture'),
    path('supprimer/<int:pk>/', views.supprimer_facture, name='supprimer_facture'),
    path('afficher/<int:pk>/', views.afficher_facture, name='afficher_facture'),
    path('', views.liste_factures, name='liste_factures'),

    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/afficher/<int:pk>/', views.afficher_categorie, name='afficher_categorie'),
    path('categories/creer/', views.creer_categorie, name='creer_categorie'),
    path('categories/modifier/<int:pk>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:pk>/', views.supprimer_categorie, name='supprimer_categorie'),

    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/afficher/<int:pk>/', views.afficher_client, name='afficher_client'),
    path('clients/creer/', views.creer_client, name='creer_client'),
    path('clients/modifier/<int:pk>/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/<int:pk>/', views.supprimer_client, name='supprimer_client'),
    path('clients/<int:client_id>/creer_facture/', views.creer_facture, name='creer_facture')
]
