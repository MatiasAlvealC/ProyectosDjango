from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label= 'Nombre y Apellido', required= True, min_length=5, max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Introduzca sus datos'}))
    email = forms.CharField(label= 'Correo Electrónico', required= True, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Introduzca su email'}))
    message = forms.CharField(label= 'Mensaje', required= True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escriba su me...','rows':5}))