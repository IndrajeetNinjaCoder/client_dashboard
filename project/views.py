from django.shortcuts import render

# Create your views here.
def projectHome(request):
    return render(request, 'project/project.html')

def newproject(request):
    return render(request, 'project/newproject.html')
