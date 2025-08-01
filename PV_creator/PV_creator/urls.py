"""
URL configuration for PV_creator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from creare_pv import views



urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('pv_creator/', views.pv_creator, name='pv_creator'),
    path('inventar/', views.inventar, name='inventar'),
    path('about/', views.about, name='about'),
    path('objectTypes/', views.objectTypes, name='objectTypes'),
    path('departaments/', views.departaments, name='departaments'),
    path('admin/', admin.site.urls),
]

if not settings.TESTING:
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()