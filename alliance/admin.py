from django.contrib import admin
from .models import Personn
# Register your models here.

class AdminPerson(admin.ModelAdmin):
    list_display = ('l_name','f_name','birthday','post','phone')
    
admin.site.register(Personn, AdminPerson)
