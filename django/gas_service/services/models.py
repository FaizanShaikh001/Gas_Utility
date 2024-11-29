from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Leak', 'Gas Leak'),
        ('Maintenance', 'Maintenance Request'),
        ('Billing', 'Billing Issue'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    
    customer = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=255, default="Unknown")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_requests')


    def save(self, *args, **kwargs):
        if self.status == 'Resolved' and not self.resolved_at:
            self.resolved_at = now()
        super(ServiceRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} - {self.request_type} ({self.status})"
