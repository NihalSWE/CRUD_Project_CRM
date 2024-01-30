from django.contrib import admin
from .models import ClientData
# Register your models here.

@admin.register(ClientData)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name','email','phone','address','city','country')
    search_fields = ['first_name','last_name','country']