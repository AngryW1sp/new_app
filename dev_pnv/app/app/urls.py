from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('', include('main.urls', namespace='main')),

] + debug_toolbar_urls() + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
