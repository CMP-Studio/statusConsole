from django.shortcuts import render, get_object_or_404
from updateProject import updateProjects, pingProject
from models import Project
from django.http import JsonResponse

# Create your views here.
def home(request):
    updateProjects()
    projects = Project.objects.all().order_by('-status')
    context = {'projects': projects}
    return render(request, "index.html" , context)

def ping(request, slug):
    proj = get_object_or_404(Project, url=slug)
    pingProject(proj, request)
    return JsonResponse({'project':proj.name, 'pinged': True})
