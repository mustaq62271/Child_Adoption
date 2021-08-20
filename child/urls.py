from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('addchild/',views.addchild,name='addchild'),
    path('removechild/',views.removechild,name='removechild'),
    path('eligible/',views.eligible,name='eligible'),
    path('documents/',views.documents,name='documents'),
    path('childs/',views.childs,name='childs'),
]
