from django.shortcuts import render
from django.urls import reverse
from .forms import contactForm
from django.core.mail import EmailMessage

def contact(request):
    contact_form = contactForm()

    return render(request, 'contact/contact.html', {'form':contact_form})