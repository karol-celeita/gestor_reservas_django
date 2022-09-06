from django import forms
from .models import Usuarios


class Reservaciones(forms.ModelForm):
	class Meta:
		model = Usuarios
		fields=['correo','nombre','fecha_reserva','area']
		widgets = {
			'correo':forms.TextInput(
				attrs={
					'class':'input-text js-input',
					'id':'title' ,
     				'placeholder':'Ingresa tu correo buho.media' 
                     }),
			'nombre':forms.TextInput(
				attrs={
					'class':'input-text js-input',
					'id':'description',      
				}),
   
			'area':forms.Select(
					attrs={
						'class':'input-text js-input',
						'id':'description',						
					}),
   
            'fecha_reserva':forms.DateInput(
				attrs={ 
                'class':'form-control js-input' ,
                'placeholder':'YYYY-MM-DD'
                }),
			}