from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import ChildTable
# Create your views here.
def home (request):
    return render(request,'index.html')

def addchild (request):
    if request.method=='POST':
        name=request.POST.get('name')
        childid=request.POST.get('childid')
        division=request.POST.get('division')
        district=request.POST.get('district')
        contact=request.POST.get('contact')
        address=request.POST.get('address')

        data=ChildTable()
        data.name=name
        data.childid=childid
        data.division=division
        data.district=district
        data.contact=contact
        data.address=address
        data.save()
        messages.success(request, 'New Child has been added successfully.')
    return render(request,'addchild.html')

def removechild (request):
    return render(request,'removechild.html')

def eligible (request):
    return render(request,'eligible.html')

def documents (request):
    return render(request,'documents.html')

def childs (request):
    child=ChildTable.objects.all()
    context={
        'data':child,
    }
    return render(request,'childlist.html',context)
