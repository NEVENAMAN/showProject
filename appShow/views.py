from django.shortcuts import render,redirect
from appShow import models

def show_detailes(request):
    show = models.show_Show_detailes(request)
    context = {
        "show" : show
    }
    return render(request,'index.html',context)

def add_show_page(request):
    return render(request,'addShow.html')

def add_show_process(request):
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
    if request.method == "GET":
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
        relase_date = id[0].relase_date
        title = id[0].title
        network = id[0].network
        desc = id[0].desc
        context = {
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
    if request.method == "POST":
        models.update_show_process(request)
    return redirect('/')