from django.contrib import admin
from .models import Venta, DetalleVenta
from django_pdf_actions.actions import export_to_pdf_portrait, export_to_pdf_landscape

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente','fecha','total')
    search_fields = ('cliente','fecha')
    actions = [export_to_pdf_portrait, export_to_pdf_landscape]

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta','producto','cantidad','precio')
    search_fields = ('venta','producto')
    actions = [export_to_pdf_portrait, export_to_pdf_landscape]

