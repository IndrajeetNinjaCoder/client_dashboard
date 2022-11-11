from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from client.models import Client
from project.models import Project

# Create your views here.
def home(request):
    return render(request, 'home/home.html')



# Authentication APIs 
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters 
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # # Checks for errorneous input
        # if len(username) > 15:
        #     messages.error(request, "Username must be under 10 characters")
        #     return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, "Username should contain letters and numbers")
        #     return redirect('home')

        # if pass1 != pass2:
        #     messages.error(request, "Passwords do not match")
        #     return redirect('home')


        # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        # messages.success(request, "Your account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 Not Found')
    


def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("404 - Not Found")

    return HttpResponse('404 Not Found')

def handleLogout(request):
    logout(request)
    # messages.success(request, "Successfully Logged Out")
    return redirect('home')

def dashboard(request):

    totalClients = Client.objects.all().count()
    totalProjects = Project.objects.all().count()
    completedProjects = Project.objects.filter(work_status="complete").count()

    incomplete = totalProjects - completedProjects

    print(f"Total Clients: {totalClients}")
    print(f"completed projects: {completedProjects}")

    return render(request, 'home/dashboard.html', {'totalClients':totalClients, 'totalProjects': totalProjects, 'completedProjects':completedProjects, 'incomplete': incomplete})

