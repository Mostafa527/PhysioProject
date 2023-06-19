from django.urls import path
from . import views
from .views import *

urlpatterns = [

path('ExercisePlan/<int:pk>',exerciseplan_detail.as_view(),name='exerciseplan_detail'),
path('ExercisePlan',views.ExercisePlanList.as_view(),name='exerciseplan_list'),
path('ExercisePlan/Patient/<int:patient_id>',views.ExercisePlanDetailsByPatient,name='ExercisePlanDetailsByPatient'),
]