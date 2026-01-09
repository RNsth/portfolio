
# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
def base_view(request):
    return render(request, 'main/base.html') 
def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"""
            Name: {name}
            Email: {email}

            Message:
            {message}
            """

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['aryan@blondmail.com'],  
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  

    else:
        form = ContactForm()

    return render(request, "main/contact.html", {"form": form})

