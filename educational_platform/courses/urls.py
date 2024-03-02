from django.urls import path

from .views import *

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),
    path('accesses/', AccessAPIView.as_view()),
    path('accesses/<int:pk>/', AccessAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
    path('lessons/<int:pk>/', LessonAPIView.as_view()),
    path('groups/', GroupAPIView.as_view()),
    path('groups/<int:pk>/', GroupAPIView.as_view()),
]
