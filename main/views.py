
# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm
def base_view(request):
    return render(request, 'main/base.html') 
def home_view(request):
    return render(request, 'main/home.html')

def about_view(request):
    return render(request, 'main/about.html')

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            form = ContactForm() 
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})
