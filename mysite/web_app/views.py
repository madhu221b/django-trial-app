from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('firstname')
    serializer_class = StudentSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")