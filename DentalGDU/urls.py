"""
URL configuration for DentalGDU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Dental_GDU import views
from Dental_GDU.views import add_person
from django.shortcuts import redirect, get_object_or_404
from Dental_GDU.forms import NoteForm


urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration_view, name='registration'),
    path('patient/<int:patient_id>/', views.patient_details_view, name='patient_details'),
    path('hello/', views.hello_view, name='hello'),
    path('home/', views.home, name='home'),
    path('add-person/', add_person, name='add_person'),
    path('add_note/', views.add_note, name='add_note'),
    path('view_notes/', views.view_notes, name='view_notes'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
 
    
]
