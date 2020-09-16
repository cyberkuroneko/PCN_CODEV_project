from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView
from .models import Projects


# Create your views here.
class ProjectsHomePageView(ListView):
    template_name = 'projects_home.html'
    model = Projects

class ProjectsInsertView(DetailView):
    template_name = 'projects_insert.html'  
    model = Projects  
    fields =['ID','company_name','sales_rep','project_name','needed_skill','other_skill','company_address','period','job_detail','needed_member']