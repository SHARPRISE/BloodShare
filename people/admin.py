from django.contrib import admin

from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'username', 'email', 'blood_type', 'phone')
    list_display = ('name', 'username', 'email', 'blood_type', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'username', 'email', 'blood_type')

admin.site.register(User, UserAdmin)
