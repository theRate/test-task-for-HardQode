from rest_framework import generics

from .serializers import *


# Create your views here.
class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AccessAPIView(generics.ListCreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


class LessonAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class GroupAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
