
from django.urls import path
from .views import *
from . import views

urlpatterns = [

path('Observation/Session/<int:session_id>',views.ObservationDetailsBySession,name='ObservationDetailsBySession'),
path('Observation/<int:pk>',observ_detail.as_view(),name='observation_detail'),
path('Observation',ObservationList.as_view(),name='observation_list'),
]