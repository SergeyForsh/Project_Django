from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Новое сообщение от {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = ['admin@example.com']
            send_mail(subject, message, sender, recipients)
            return render(request, 'main/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
