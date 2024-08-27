from django.urls import path
from goods import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),

] + debug_toolbar_urls()
