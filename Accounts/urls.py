
from django.urls import path
from .views import *
urlpatterns = [
  path('login/', LoginView.as_view(), name='login'),
  path('User_Logout2/', Logout.as_view(), name='logout'),
  path('user_logout/', LogoutView.as_view(), name='logout_view'),
  path('user_list/', RegisterView.as_view(), name="register"),
  path('user_detail/<int:pk>', user_detail.as_view(), name='user_detail'),

]