from django.contrib import admin
from .models import *

@admin.register(Usuarios)
class HeroAdmin(admin.ModelAdmin):
    list_filter = ('fecha_reserva',)
    date_hierarchy = 'fecha_reserva'
    list_display = ('correo', 'nombre','fecha_reserva','area')


class ReservacionAdmin(admin.ModelAdmin):
	list_display = ('dias', 'puestos')
	readonly_fields = ("dias",)
	#limita el numero registros desde el admin
	def has_add_permission(self, request):
		num_objects = self.model.objects.count()
		if num_objects >= 6:
			return False
		else:
			return True


admin.site.register(Reservacion,ReservacionAdmin)
admin.site.register(Area)
