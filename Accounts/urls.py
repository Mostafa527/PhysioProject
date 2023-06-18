
from django.urls import path
from .views import *
urlpatterns = [

  path('user_list/', RegisterView.as_view(), name="register"),

]