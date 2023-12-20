from django.contrib import admin
from .models import ejra, rooydad, sans, review


# Register your models here.
class ejraAdmin(admin.ModelAdmin):
    search_fields = ['title',]
    list_filter = ['start_sale_date',]
    
admin.site.register(ejra, ejraAdmin)
admin.site.register(rooydad)
admin.site.register(sans)
admin.site.register(review)