from django.contrib import admin
from core.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username']
admin.site.register(User,UserAdmin)