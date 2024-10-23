from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
    
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nom

class Facture(models.Model):
    numero = models.CharField(max_length=50)
    date_emission = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    est_payee = models.BooleanField(default=False)

    def __str__(self):
        return f"Facture {self.numero} - {self.montant}€"