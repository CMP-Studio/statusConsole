from django.shortcuts import render
from updateProject import updateProjects, pingProject
from models import Project

# Create your views here.
def home(request):
    updateProjects()
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "index.html" , context)

def ping(request, slug):
    proj = get_object_or_404(Project, url=slug)
    pingProject(project, request)
