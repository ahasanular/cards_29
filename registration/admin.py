from django.contrib import admin
from .models import AppUser


# Register your models here.
class AppUserAdmin(admin.ModelAdmin):
    fields = ['user', 'full_name', 'email', 'slug']
    list_display = ['user', 'full_name', 'email', 'slug']
    readonly_fields = ['slug']

admin.site.register(AppUser, AppUserAdmin)