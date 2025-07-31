from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', EmailLoginAPIView.as_view(), name='login'),
    path('admin/userlist/', UserListAPIView.as_view(), name='user_list'),
    path('admin/update_role/<int:user_id>/', UserRoleUpdateAPIView.as_view(), name='update_role'),


]
