from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('', include('main.urls', namespace='main')),

]
