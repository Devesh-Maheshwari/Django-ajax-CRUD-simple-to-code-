from django.shortcuts import render, redirect,get_object_or_404
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
        print(model)
        print(model.id)

        return JsonResponse(data =  {'company_name' : model.company_name, 'company_location' : model.company_location,'id':model.id})



def deleteview(request,id):
    print("gsdh jsdgjkhsdjkh gsdjkhdjk")
    if request.method=="DELETE":
        print("devesh id ldsfkljfdsl")

        company =  get_object_or_404(Company, pk=id)
        company.delete()
        return JsonResponse(data={'statusfgf':'i am well'})


def Updatecompany(request,id):
    print("!@#$%^&*(")
    comp=get_object_or_404(Company,id=id)
    if request.method=='POST':

        comp.company_name = request.POST['company_name1']
        comp.company_location = request.POST['company_location1']
        comp.save()
        return JsonResponse(
            data={'company_name': comp.company_name, 'company_location': comp.company_location, 'id': comp.id})






