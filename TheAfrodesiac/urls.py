from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'TheAfrodesiac'

urlpatterns = [
    url(r'^$', views.index_view, name='home'),
    url(r'^about/', views.about_view, name='about'),
    url(r'^fashion/', views.fashion_view, name='fashion'),
    url(r'^poetry/', views.poetry_view, name='poetry'),
    url(r'^contact/', views.contact_view, name='contact'),
    url(r'^art/', views.art_view, name='art'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

