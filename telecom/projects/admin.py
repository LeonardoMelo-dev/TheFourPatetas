from django.contrib import admin

# Register your models here.
from .models import Service, Packets, Packets_Services

admin.site.register(Service)
admin.site.register(Packets)
admin.site.register(Packets_Services)