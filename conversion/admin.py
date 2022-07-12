from django.contrib import admin
from .models import *



class ValuteAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_amount', 'from_curr', 'to_curr', 'converted_amount', 'data_converted')
    list_display_links = ('id', 'from_amount')

admin.site.register(Valute,ValuteAdmin)



