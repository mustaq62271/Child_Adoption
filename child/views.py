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
        childcode=request.POST.get('childcode')
        childage=request.POST.get('childage')
        health=request.POST.get('health')
        childweight=request.POST.get('childweight')
        childheight=request.POST.get('childheight')
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        image=request.POST.get('image')


        data=ChildTable()
        data.name=name
        data.childcode=childcode
        data.childage=childage
        data.health=health
        data.childweight=childweight
        data.childheight=childheight
        data.gender=gender
        data.blood=blood
        data.image=image
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
