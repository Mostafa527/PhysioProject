from django.urls import path
from . import views
from .views import *

urlpatterns = [

path('Session/ExercisePlan/<int:exerciseplan_id>',views.SessionByExercisePlan,name='SessionByExercisePlan'),
path('Session/<int:session_id>',views.session_detail,name='session_detail'),
path('Session',SessionList.as_view(),name='session_list'),
]