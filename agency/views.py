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

def removeagency (request, id):
    agency=AgencyTable.objects.get(id=id)
    agency.delete()
    context={
        'data':agency
    }
    messages.success(request, 'Agency has been deleted successfully.')
    return render(request,'removeagency.html',context)

def updateagency (request, id):
    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        address=request.POST.get('address')

        data=AgencyTable.objects.get(id=id)
        data.name=name
        data.contact=contact
        data.address=address
        data.save()
        messages.success(request, 'Agency has been updated successfully.')
    update=AgencyTable.objects.get(id=id)
    context={
        'data':update,
    }
    return render(request,'updateagency.html',context)

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
