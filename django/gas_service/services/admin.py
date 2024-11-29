from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at', 'resolved_at')
    list_filter = ('status', 'request_type', 'created_at')
