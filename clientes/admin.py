from django.contrib import admin
from .models import Cliente

admin.site.site_header = "Gestion Inventario"
admin.site.site_title = "Gestion Inventario"
admin.site.index_title = "Bienvenido al panel de administración"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','email','direccion')
    search_fields = ('nombre','email')