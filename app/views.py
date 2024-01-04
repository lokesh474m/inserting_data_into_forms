from django.shortcuts import render

# Create your views here.

from app.forms import *
from app.models import *
from django.http import HttpResponse

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']   
            sp=SFDO.cleaned_data['Sprincipal']
            sl=SFDO.cleaned_data['Slocation']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl)[0]
            SO.save()
            SOL=School.objects.all()
            d1={'formobjects':SOL}
            return render(request,'display_schools.html',d1)
        else:
            return HttpResponse('invalid data')
    return render(request,'create_school.html',d)




# QLTO=Topic.objects.all()
#         d={'topics':QLTO}
#         return render(request,'display_topic.html',d)