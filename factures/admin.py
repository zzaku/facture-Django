from django.contrib import admin
from .models import Facture

class FactureAdmin(admin.ModelAdmin):
    list_filter = ('client',) 
    search_fields = ('client__nom', 'nom')
    actions = ['marquer_comme_payee']

    def marquer_comme_payee(self, request, queryset):
        queryset.update(est_payee=True)
        self.message_user(request, f'{queryset.count()} factures ont été marquées comme payées.')
    
    marquer_comme_payee.short_description = 'Marquer comme payée les factures sélectionnées'

admin.site.register(Facture, FactureAdmin)