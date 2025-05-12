from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, Proveedor


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'mostrar_imagen')
    search_fields = ('nombre', 'precio')
    readonly_fields = ('mostrar_imagen',)
    
    def mostrar_imagen(self, obj):
        if obj.img:
            return format_html('<img src="{}" width="100" height="100" />', obj.img.url)
        return 'Sin imagen'
    
    mostrar_imagen.short_description = 'Imagen'

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','email','direccion')
    search_fields = ('nombre','telefono')
