from django.urls import path
from .views import *
from . import views

urlpatterns = [
path('Physio/<int:pk>',physio_detail.as_view(),name='physio_detail'),
path('Physio',PhysioList.as_view(),name='physioList'),
path('Physio/Patient/<int:patient_id>',views.therpyDetailsByPatient,name='TherpyDetailsByPatient'),
path('Physio/Clinic/<int:clinic_id>',views.therpysDetailsByClinic,name='TherpyDetailsByClinic'),
]