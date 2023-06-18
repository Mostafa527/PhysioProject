
from django.urls import path
from .views import *
urlpatterns = [

  path('user_list/', RegisterView.as_view(), name="register"),
  path('user_detail/<int:pk>', user_detail.as_view(), name='user_detail'),

]