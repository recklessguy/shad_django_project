from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required
from .views import addwriting

urlpatterns = [
    path("", views.home, name='home'), 
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("new_ghazals", views.newghazals, name='new-ghazals'),
    path("famous_ghazals", views.famousghazals, name='famous-ghazals'),
    path("search", views.search_for, name='search'),
    path("admin/", views.admin, name='admin'),
    path("add_writings",login_required(addwriting.as_view(template_name='add_writings.html')), name='add_writings'),
]
