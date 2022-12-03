from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

# Register your models here.
# admin.site.register(NewUser , UserAdmin)

fields = list(UserAdmin.fieldsets)
fields[1] = ( 'Personal Info' , { 'fields' : ('first_name', 'last_name', 'email' ,'api_key', 'Doctor_attending', 'date_of_visit','last_date_of_visit') })
UserAdmin.fieldsets = tuple(fields)

admin.site.register(NewUser , UserAdmin)
