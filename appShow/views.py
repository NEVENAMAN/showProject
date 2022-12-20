from django.shortcuts import render,redirect
from appShow import models
from django.contrib import messages
from .models import Show


def show_detailes(request):
    show = models.show_Show_detailes(request)
    context = {
        "show" : show
    }
    return render(request,'index.html',context)

def add_show_page(request):
    return render(request,'addShow.html')
# ------------------------------------------------------------validation
def add_show_process(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/add_show_page')
    else:
        if request.method == "POST":
            models.create_show(request)
        return redirect('/')

def get_show_data(request):
    show = models.show_Show_detailes(request)
    context = {
        "show" : show
    }
    return render(request,'editshow.html',context)

def show_info(request):
    show = models.show_Show_detailes(request)
    context = {
        "show" : show
    }
    return render(request,'show.html',context)

def show_page(request):
    if request.method == "POST":
        id = models.show_show(request)
    context = {
        "show" : id[0] 
    }
    for sh in id :
        print(sh.id)
        print(sh.title)
    return render(request,'show.html',context)

def edit_show(request):
    if request.method == "POST":
        id = models.edit_show(request)
        show_id = id[0].id
        relase_date = id[0].relase_date
        title = id[0].title
        network = id[0].network
        desc = id[0].desc
        context = {
            "show_id" : show_id,
            "relase_date" : relase_date,
            "title" : title,
            "network" : network,
            "desc" : desc,
        }
        return render(request,'editshow.html',context)
    
def delete_show(request):
    if request.method == "POST":
        models.delete_show(request)
    return redirect('/')

def update_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/add_show_page')
    else:
        if request.method == "POST":
            models.update_show_process(request)
        return redirect('/')