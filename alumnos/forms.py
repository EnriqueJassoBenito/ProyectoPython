from django import forms
from .models import Alumno

class alumnoForms(forms.ModelForm):
    class Meta:
        model = Alumno

        fields = ['nombre', 'apellido', 'edad', 'matricula', 'correo']
        id = forms.CharField(widget=forms.HiddenInput(), required=False)
        widgets = { 
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'forms-input',
                    'placeholder': 'Nombre del alumno'
                }
            ),
            'apellido': forms.TextInput(
                attrs= {
                    'class': 'forms-input',
                    'placeholder': 'Ingrese sus apellidos'
                }
            ),
            'edad': forms.NumberInput(
                attrs= {
                    'class': 'forms-input',
                    'placeholder': 'Ingrese su edad'
                }
            ),
            'matricula': forms.TextInput(
                attrs= {
                    'class': 'forms-input',
                    'placeholder': 'Ingrese su matricula'
                }
            ),
            'correo': forms.TextInput(
                attrs= {
                    'class': 'forms-input',
                    'placeholder': 'Ingrese su correo electronico'
                }
            ),
        }

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad': 'Edad',
            'matricula': 'Matricula',
            'correo': 'Correo'
        }

        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio.'
            },
            'apellido': {
                'required': 'El apellido es obligatorio.'
            },
            'edad': {
                'required': 'La edad es obligatoria.',
                'invalid': 'Ingresa una edad válida.'
            },
            'matricula': {
                'required': 'La matrícula es obligatoria.',
                'invalid': 'Ingresa una matrícula válida.'
            },
            'correo': {
                'required': 'El correo es obligatorio.',
                'invalid': 'Ingresa un correo electrónico válido.'
        }
    }
