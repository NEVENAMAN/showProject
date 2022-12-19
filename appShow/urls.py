from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_detailes),
    path('add_show_page',views.add_show_page),
    path('add_show_process',views.add_show_process),
    path('get_show_data',views.get_show_data),
    path('show_info',views.show_info),
    path('show_page',views.show_page),
    path('edit_show',views.edit_show),
    path('delete_show',views.delete_show),
    path('update_show',views.update_show),
]