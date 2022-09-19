from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import  CreateView
from .models import *
from datetime import  datetime
from django.views.generic.list import ListView
from django.db.models import Count


class ReservacionUsuario(CreateView):
	model = Usuarios
	form_class = Reservaciones
	template_name = 'index.html'
	success_url = reverse_lazy('home')
	success_message = 'Se ha creado con éxito'

	def form_valid(self, form):
		messages.success(self.request, self.success_message, extra_tags='God Job')
		return super().form_valid(form)

	def form_invalid(self, form):
		lista = ""
		for error in form.errors:
			lista+=str(error)

		#https://stackoverflow.com/questions/43588876/how-can-i-add-additional-data-to-django-messages
		messages.error(self.request, '%s debido a un error en el campo de: %s' % (self.error_message, lista), extra_tags='Error')
		return redirect(str(self.success_url))


	#Validación que limpia el los input de un espacio inicial y final con strip al guardar
	#https://www.peterbe.com/plog/automatically-strip-whitespace-in-django-forms
 
	def clean(self):
		for field in self.cleaned_data:
			if isinstance(self.cleaned_data[field], basestring):
				self.cleaned_data[field] = self.cleaned_data[field].strip()
		return self.cleaned_data


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST) #cargo los datos del formulario

		fecha=request.POST.get('fecha_reserva')
		correo=request.POST.get('correo')
  
		date_time_obj = datetime.strptime(fecha, '%Y-%m-%d')
		dia_reserva = date_time_obj.strftime('%A')

		reservas_actuales=Usuarios.objects.filter(fecha_reserva=fecha).count()
		reservas_totales= Reservacion.objects.filter(dias=dia_reserva).values_list('puestos',flat=True)[0]

		if Usuarios.objects.filter(fecha_reserva=fecha, correo=correo).exists():
			print("Usuario ya registrado")
			messages.error(self.request, 'Ya existe una reserva asignada a este usuario, intenta con un correo diferente', extra_tags='Error')
			return super().form_valid(form)

		else:
			if reservas_actuales <= reservas_totales:
				print("hay puesto")
				if form.is_valid():
					print("es valido")
					form.save()
					return self.form_valid(form)
				else:
					self.form_invalid(form)
			else:
				print("no hay puesto")
				messages.error(self.request, 'No hay espacios disponibles para esta fecha, prueba una fecha diferente', extra_tags='Error')
				return super().form_valid(form)
	
		return redirect(str(self.success_url))


class ListaReservas(ListView):
    model = Usuarios
    template_name = 'lista_reservas.html'
    context_object_name = 'data'
    queryset= Usuarios.objects.all().values('fecha_reserva').annotate(total=Count('fecha_reserva')).order_by('fecha_reserva')
    
    def get_context_data(self, **kwargs):
        context = super(ListaReservas, self).get_context_data(**kwargs)
        context.update({
            'character_universe_list':  Usuarios.objects.all().values('fecha_reserva').annotate(total=Count('fecha_reserva')).order_by('fecha_reserva'),
            'more_context': Reservacion.objects.all(),
        })
        return context
    
    
    def get_queryset(self):
        return  Usuarios.objects.all().values('fecha_reserva').annotate(total=Count('fecha_reserva')).order_by('fecha_reserva' )
