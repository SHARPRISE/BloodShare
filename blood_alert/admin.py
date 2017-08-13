from django.contrib import admin

from .models import Alert
# Register your models here.

class AlertAdmin(admin.ModelAdmin):
    fields = ('name', 'blood_type', 'phone', 'location', 'resolved')
    list_display = ('name', 'blood_type', 'phone', 'location', 'resolved')
    list_filter = ('resolved',)
    date_hierarchy = 'date_posted'
    ordering = ('name', 'blood_type',)
    search_fields = ('name', 'blood_type',)

admin.site.register(Alert, AlertAdmin)
