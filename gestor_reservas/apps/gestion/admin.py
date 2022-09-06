from django.contrib import admin
from .models import *

@admin.register(Usuarios)
class HeroAdmin(admin.ModelAdmin):
    list_filter = ('fecha_reserva',)
    date_hierarchy = 'fecha_reserva'
    

admin.site.register(Reservacion)
admin.site.register(Area)
