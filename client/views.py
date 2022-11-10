from django.shortcuts import render

# Create your views here.
def clientHome(request):
    return render(request, 'client/client.html')


def newclient(request):
    return render(request, 'client/newClient.html')