from django.urls import path
from .views import base_view, home_view, about_view, contact_view

urlpatterns = [
    path('', base_view, name='base'),        # Root URL → base.html
    path('home/', home_view, name='home'),   # /home/ → home.html
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]