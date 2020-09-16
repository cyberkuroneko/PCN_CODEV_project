from django.urls import path
from .views import ProjectsHomePageView,ProjectsInsertView

# from .views import ProjectsInsertPageView

urlpatterns = [
    
    path('',ProjectsHomePageView.as_view(),name='projects_home'),
    path('projects/projects_insert/',ProjectsInsertView.as_view(),name='projects_insert'),
]