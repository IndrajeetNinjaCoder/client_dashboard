from django.shortcuts import render, HttpResponse, redirect
from .models import Client

# Create your views here.
def clientHome(request):
    totalClients = Client.objects.all().count()
    currentClients = Client.objects.all().count()

    return render(request, 'client/client.html', {'totalClients': totalClients, 'currentClients': currentClients})


def createclient(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        phone = request.POST['phone']
        email = request.POST['email']

        client = Client(name=name, company=company, phone=phone, email=email)

        client.save();
       
        return redirect('clientHome')

    return HttpResponse("404 Not Found")


