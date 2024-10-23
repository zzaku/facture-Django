from django.urls import reverse
from django.test import TestCase
from .models import Facture

class FactureModelTest(TestCase):
    
    def setUp(self):
        self.facture = Facture.objects.create(
            numero="F001",
            date_emission="2024-12-10",
            montant_ht=100.00,
            tva=20.00
        )

    def test_creation_facture(self):
        """Test de création d'une facture"""
        self.assertEqual(self.facture.numero, "F001")
        self.assertEqual(self.facture.montant_ht, 100.00)
        self.assertEqual(self.facture.tva, 20.00)

    def test_str_representation(self):
        """Test de la représentation en chaîne de la facture"""
        self.assertEqual(str(self.facture), "Facture F001")

    def test_calcul_total_ttc(self):
        """Test du calcul du total TTC"""
        total_ttc = self.facture.montant_ht + (self.facture.montant_ht * (self.facture.tva / 100))
        self.assertEqual(total_ttc, 120.00)

class FactureListViewTest(TestCase):

    def setUp(self):
        Facture.objects.create(numero="F001", montant_ht=100, tva=20)
        Facture.objects.create(numero="F002", montant_ht=200, tva=20)

    def test_list_view_status_code(self):
        response = self.client.get(reverse('facture_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_template(self):
        response = self.client.get(reverse('facture_list'))
        self.assertTemplateUsed(response, 'facture_list.html')

    def test_factures_in_context(self):
        response = self.client.get(reverse('facture_list'))
        self.assertTrue(len(response.context['factures']) == 2)

class FactureDetailViewTest(TestCase):

    def setUp(self):
        self.facture = Facture.objects.create(numero="F001", montant_ht=100, tva=20)

    def test_detail_view_status_code(self):
        url = reverse('facture_detail', args=[self.facture.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_template(self):
        url = reverse('facture_detail', args=[self.facture.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'facture_detail.html')

    def test_facture_in_context(self):
        url = reverse('facture_detail', args=[self.facture.id])
        response = self.client.get(url)
        self.assertEqual(response.context['facture'], self.facture)

class FactureCreateViewTest(TestCase):

    def test_create_view_status_code(self):
        """Test que la vue de création renvoie un code 200"""
        response = self.client.get(reverse('facture_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_view_template(self):
        """Test que la vue de création utilise le bon template"""
        response = self.client.get(reverse('facture_create'))
        self.assertTemplateUsed(response, 'facture_form.html')

    def test_valid_facture_creation(self):
        """Test la création d'une facture valide"""
        response = self.client.post(reverse('facture_create'), {
            'numero': 'F003',
            'montant_ht': 150,
            'tva': 20
        })
        self.assertEqual(Facture.objects.count(), 1)
        self.assertRedirects(response, reverse('facture_list'))