from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q


from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student
from django.views.generic import TemplateView, ListView
from django.template import RequestContext
from django.shortcuts import render

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('firstname')
    serializer_class = StudentSerializer


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Student
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        name = self.request.GET.get('q_name')
        # If the name sent is a full name with a space.
        name_arr = name.split(" ")
        object_list = list()
        if len(query.strip()) != 0:
            object_list = Student.objects.filter(id=int(query))
        elif len(name_arr) == 2:
            object_list = Student.objects.filter(Q(firstname__icontains=name_arr[0]) &
                                                 Q(lastname__icontains=name_arr[1]))
        elif len(name.strip()) != 0:
            object_list = Student.objects.filter(Q(firstname__icontains=name) |
                                                  Q(lastname__icontains=name))
        return object_list




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")