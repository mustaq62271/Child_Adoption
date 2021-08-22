from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import ClientTable

# Create your views here.
def clientdetails (request):
    client=User.objects.all()
    context={
        'data':client,
    }
    return render(request,'clientdetails.html',context)

def registration (request):
    return render(request,'child-reg.html')
