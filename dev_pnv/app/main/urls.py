from django.urls import path
from main import views
from debug_toolbar.toolbar import debug_toolbar_urls


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('payidel', views.pay_and_deliver, name='pay_and_deliver'),
    path('contacts', views.contacts, name='contacts'),

] + debug_toolbar_urls()
