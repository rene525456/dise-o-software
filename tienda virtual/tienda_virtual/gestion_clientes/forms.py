from django import forms
from modelo.models import Cliente

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "correo", "telefono", "celular", "direccion"]
        widgets = {
            'cedula': forms.TextInput(attrs={'placeholder':'Ingrese Cédula', 'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'placeholder':'Ingrese Apellidos', 'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'placeholder':'Ingrese Nombres', 'class': 'form-control'}),
            'genero': forms.RadioSelect(attrs={'class': "form-check-input"}),
            'correo': forms.TextInput(attrs={'placeholder': 'Ingrese Correo Electrónico', 'class': 'form-control col-md-8', 'type': 'email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese Teléfono','class': 'form-control col-md-8'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ingrese Celular','class': 'form-control col-md-8'}),
            'direccion': forms.Textarea(attrs={'placeholder': 'Ingrese Dirección','class': 'form-control', 'rows':'4', 'type':'area'}),
        }
