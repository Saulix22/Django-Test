from django.contrib import admin
from .models import Material, Solicitud

class SolicitudAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)

# Register your models here.
admin.site.register(Material)
admin.site.register(Solicitud, SolicitudAdmin)

