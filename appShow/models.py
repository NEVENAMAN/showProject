import datetime
import time
from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        len_titles = len(Show.objects.filter(title = postData['title']))

        # relase_date = postData['relase_date']
        # print(relase_date)
        # local_date = datetime.date.today()
        # print("local date------")
        # print(local_date)
        # print(local_date == datetime.date.fromtimestamp(time.time()))
        # datee = time.strptime(relase_date, "%Y-%m-%d") 
        # # local = time.strptime(local_date, "%Y-%m-%d") 
        # # print(abs(datee - local_date))
        # print("date------------")
        # print(datee)
       
        print
        if len(postData['title']) < 3 :
            errors['title'] = "Show title should be at least 3 characters."
        if len_titles > 0 :
            errors['titleunqiue'] = "Show title name must be unique"     
        if len(postData['network']) < 3 :
            errors['network'] = "Show network should be at least 3 characters"
        if ((datetime.datetime.strptime(postData['relase_date'], '%Y-%m-%d')) > (datetime.datetime.today())):
            errors['relase_date'] = "Show Relase date should brfore local date"
        if len(postData['desc']) < 5 :
            errors['desc'] = "Show description should be at least 5 characters" 
        return errors

class Show(models.Model):
    title = models.CharField(max_length=60,unique=True)
    network = models.TextField(max_length=60)
    desc = models.TextField()
    relase_date = models.DateTimeField(auto_now=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

def show_Show_detailes(request):
    return Show.objects.all()

def create_show(request):
    title = request.POST['title']
    network = request.POST['network']
    relase_date = request.POST['relase_date']
    desc = request.POST['desc']
    return Show.objects.create(title = title , network = network,desc = desc , relase_date = relase_date)

def show_show(request):
    id = request.POST['show_show_id']
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
    title_edit = request.POST['title']
    network_edit = request.POST['network']
    relase_date_edit = request.POST['relase_date']
    desc_edit = request.POST['desc']
    print(id)
    print(title_edit)
    print(network_edit)
    print(relase_date_edit)
    print(desc_edit)
    show = Show.objects.get(id = id )
    show.title = title_edit 
    show.network = network_edit
    show.relase_date = relase_date_edit
    show.desc = desc_edit
    return show.save()

    
