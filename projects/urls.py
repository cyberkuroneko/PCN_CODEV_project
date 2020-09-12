from django.urls import path
from .views import ProjectsHomePageView

urlpatterns = [
    path('',ProjectsHomePageView.as_view(),name='projects_home'),
]