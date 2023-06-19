from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
path('Patient/<int:pk>',patient_detail.as_view(),name='patient_detail'),
path('Patient',PatientList.as_view(),name='patient_list'),
path('Patient/Physiotherapist/<int:physio_id>',views.PatientsDetailsByTherpy,name='PatientDetailsByTherpy'),
]