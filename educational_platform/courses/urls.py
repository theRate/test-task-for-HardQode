from django.urls import path

from .views import ProductAPIView, LessonAPIView, GroupAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('lessons/', LessonAPIView.as_view()),
    path('groups/', GroupAPIView.as_view())
]
