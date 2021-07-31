from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import AgencyTable
# Create your views here.
def home (request):
    return render(request,'index.html')

def addagency (request):
    if request.method=='POST':
        name=request.POST.get('name')
        division=request.POST.get('division')
        district=request.POST.get('district')
        contact=request.POST.get('contact')
        address=request.POST.get('address')

        data=AgencyTable()
        data.name=name
        data.division=division
        data.district=district
        data.contact=contact
        data.address=address
        data.save()
        messages.success(request, 'New agency has been added successfully.')
    return render(request,'addagency.html')

def removeagency (request):
    return render(request,'removeagency.html')

def updateagency (request):
    return render(request,'updateagency.html')

def eligible (request):
    return render(request,'eligible.html')

def documents (request):
    return render(request,'documents.html')

def agencies (request):
    agency=AgencyTable.objects.all()
    context={
        'data':agency,
    }
    return render(request,'agencylist.html',context)
