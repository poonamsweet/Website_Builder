from django.urls import path
from .views import *

urlpatterns = [
    path('generate/', GenerateWebsiteAPIView.as_view()),
    path('websites/', WebsiteListCreateAPIView.as_view()),
    path('websites/<str:pk>/', WebsiteDetailAPIView.as_view()),
    path('preview/<str:id>/', preview_website, name='preview'),

]
