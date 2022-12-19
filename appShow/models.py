from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=60)
    network = models.TextField(max_length=60)
    desc = models.TextField()
    relase_date = models.DateTimeField(auto_now=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def show_Show_detailes(request):
    return Show.objects.all()

def create_show(request):
    title = request.POST['title']
    network = request.POST['network']
    relase_date = request.POST['relase_date']
    desc = request.POST['desc']
    return Show.objects.create(title = title , network = network,desc = desc , relase_date = relase_date)

def show_show(request):
    id = request.GET['show_show_id']
    return Show.objects.filter(id = id)

def edit_show(request):
    id = request.POST['edit_show_id']
    return Show.objects.filter(id = id)

def delete_show(request):
    id = request.POST['delete_show_id']
    element_id = Show.objects.get(id = id )
    return element_id.delete()

def update_show_process(request):
    id = request.POST['edit_show_id']
    title_edit = request.POST['title_edit']
    network_edit = request.POST['network_edit']
    relase_date_edit = request.POST['relase_date_edit']
    desc_edit = request.POST['desc_edit']
    show = Show.objects.get(id = id)
    show.title = title_edit 
    show.network = network_edit
    show.relase_date = relase_date_edit
    show.desc = desc_edit
    return show.save()

    
