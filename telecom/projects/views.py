from multiprocessing import context
from django.forms import ModelForm
from django.shortcuts import render, redirect


import projects
from .models import Service
from .forms import ProjectForm

def service(request):
    service = Service.objects.all()
    return render(request , 'projects/service.html', {'servicos': service})

def teste(request):
    teste1 = Service.objects.all()
    return render(request , 'projects/teste.html', {'teste': teste1})


def information(request, pk):
    project = Service.objects.get(Id=pk)
    return render(request , 'projects/information.html', {'informacao':project})

def createProject(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service')
            
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Service.objects.get(Id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('service')
            
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project = Service.objects.get(Id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('service')
    context = {'object': project}
    return render(request, 'projects/delete_object.html', context)