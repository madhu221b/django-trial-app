from django.urls import path, include
from rest_framework import routers
from . import views

from .views import HomePageView, SearchResultsView

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)

urlpatterns = [
    path('index', views.index, name='index'),
    path('', include(router.urls)),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('home/', HomePageView.as_view(), name='home'),
]