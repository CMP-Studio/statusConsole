from django.shortcuts import render
from updateProject import updateProjects
from models import Project

# Create your views here.
def home(request):
    updateProjects()
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "index.html" , context)
