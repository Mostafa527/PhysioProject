from django.urls import path, include
from .views import *

urlpatterns = [
path('MyAdmin/<int:pk>',admin_detail.as_view(),name='admin_detail'),
path('MyAdmin',adminList.as_view(),name='admin_list'),
]