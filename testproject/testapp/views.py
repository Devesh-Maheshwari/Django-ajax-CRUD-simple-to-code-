from django.shortcuts import render, redirect
from .models import Company
from django.urls import reverse
import json
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect

def company(request):
    company_list=Company.objects.all()
    context={'company_list':company_list}
    return render(request,'testapp/details.html',context)

def Createcompany(request):
    if request.method=='POST':
        model=Company()
        model.company_name=request.POST['company_name']
        model.company_location=request.POST['company_location']
        model.save()

        return JsonResponse(data =  {'company_name' : model.company_name, 'company_location' : model.company_location})

