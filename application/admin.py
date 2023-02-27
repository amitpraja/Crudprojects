from django.contrib import admin
from application.models import Client,projects

# Register your models here.
class clientadmin(admin.ModelAdmin):
    list_display=['id','client_name','created_at','created_by']
admin.site.register(Client,clientadmin)

class projectadmin(admin.ModelAdmin):
    list_display=['project_name']
admin.site.register(projects,projectadmin)
