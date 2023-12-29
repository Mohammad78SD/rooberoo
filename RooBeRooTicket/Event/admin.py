from django.contrib import admin
from .models import Event, Sans, Review, Ticket

from django_jalali.admin.filters import JDateFieldListFilter

import django_jalali.admin as jadmin

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_filter = ['location',]
    
    

    
admin.site.register(Event, EventAdmin)
admin.site.register(Sans)
admin.site.register(Review)
admin.site.register(Ticket)