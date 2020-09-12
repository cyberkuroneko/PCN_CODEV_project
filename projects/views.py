from django.views.generic import ListView
from .models import Projects


# Create your views here.
class ProjectsHomePageView(ListView):
    template_name = 'projects_home.html'
    model = Projects