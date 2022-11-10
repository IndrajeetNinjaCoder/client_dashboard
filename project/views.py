from django.shortcuts import render, HttpResponse, redirect
from .models import Project
# Create your views here.

def projectHome(request):
    totalProjects = Project.objects.all().count()
    completeProjects = Project.objects.filter(work_status='complete').count()
    pendingProjects = Project.objects.filter(work_status='pending').count()
    ongoingProjects = Project.objects.filter(work_status='onProgress').count()

    print(f"Total Projects : {totalProjects}")
    print(f"Complete Projects : {completeProjects}")
    print(f"pending Projects : {pendingProjects}")
    print(f"ongoing Projects : {ongoingProjects}")

    return render(request, 'project/project.html', {'totalProjects':totalProjects, 'completeProjects':completeProjects, 'pendingProjects': pendingProjects, 'ongoingProjects':ongoingProjects})

def newproject(request):
    return render(request, 'project/newproject.html')

def createProject(request):
    if request.method == 'POST':
        projectId = request.POST['projectId']
        title = request.POST['title']
        department = request.POST['department']
        priority = request.POST['priority']
        client = request.POST['client']
        _from = request.POST['_from']
        _to = request.POST['_to']
        work_status = request.POST.get('work_status')

        project = Project(projectId=projectId, title=title, department=department, priority=priority, client=client, _from=_from, _to=_to, work_status=work_status)

        project.save()

        print(f"Work Status - {work_status}")
        return redirect('newproject')

    return HttpResponse("404 Not Found")