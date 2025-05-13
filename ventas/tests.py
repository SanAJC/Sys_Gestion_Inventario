from django.test import TestCase
from .models import Venta, DetalleVenta
from clientes.models import Cliente
from products.models import Producto
from datetime import date


class VentaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Cliente",
            apellido="Test",
            telefono="123456789",
            email="cliente@test.com",
            direccion="Dirección Test"
        )
        self.venta = Venta.objects.create(
            cliente=self.cliente,
            total=100.00
        )
    
    def test_venta_creation(self):
        self.assertTrue(isinstance(self.venta, Venta))
        self.assertEqual(str(self.venta), f"Venta {self.venta.id} - {self.cliente} - {self.venta.fecha}")
    
    def test_venta_fields(self):
        self.assertEqual(self.venta.cliente, self.cliente)
        self.assertTrue(isinstance(self.venta.fecha, date) or hasattr(self.venta.fecha, 'date'))
        self.assertEqual(float(self.venta.total), 100.00)


class DetalleVentaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Cliente",
            apellido="Test",
            telefono="123456789",
            email="cliente@test.com",
            direccion="Dirección Test"
        )
        
        self.venta = Venta.objects.create(
            cliente=self.cliente,
            total=100.00
        )
        
        from products.models import Proveedor
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor Test",
            telefono="987654321",
            email="proveedor@test.com",
            direccion="Dirección Proveedor"
        )
        
        self.producto = Producto.objects.create(
            nombre="Producto Test",
            precio=100.00,
            stock=10,
            proveedor=self.proveedor
        )
        
        self.detalleventa = DetalleVenta.objects.create(
            venta=self.venta,
            producto=self.producto,
            cantidad=1,
            precio=100.00
        )
    
    def test_detalleventa_creation(self):
        self.assertTrue(isinstance(self.detalleventa, DetalleVenta))
        self.assertEqual(str(self.detalleventa), f"Detalle {self.detalleventa.id} - {self.venta} - {self.producto}")
    
    def test_detalleventa_fields(self):
        self.assertEqual(self.detalleventa.venta, self.venta)
        self.assertEqual(self.detalleventa.producto, self.producto)
        self.assertEqual(self.detalleventa.cantidad, 1)
        self.assertEqual(float(self.detalleventa.precio), 100.00)

