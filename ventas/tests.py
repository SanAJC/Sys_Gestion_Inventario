from django.test import TestCase
from .models import Venta, DetalleVenta


class VentaModelTest(TestCase):
    def setUp(self):
        self.venta = Venta.objects.create(
            cliente="Cliente Test",
            fecha="2022-01-01",
            total=100.00,
            estado="Pagada"
        )
    
    def test_venta_creation(self):
        self.assertTrue(isinstance(self.venta, Venta))
        self.assertEqual(self.venta.__str__(), "Venta Test")
    
    def test_venta_fields(self):
        self.assertEqual(self.venta.cliente, "Cliente Test")
        self.assertEqual(self.venta.fecha, "2022-01-01")
        self.assertEqual(self.venta.total, 100.00)
        self.assertEqual(self.venta.estado, "Pagada")


class DetalleVentaModelTest(TestCase):
    def setUp(self):
        self.detalleventa = DetalleVenta.objects.create(
            venta="Venta Test",
            producto="Producto Test",
            cantidad=1,
            precio=100.00,
            total=100.00
        )
    
    def test_detalleventa_creation(self):
        self.assertTrue(isinstance(self.detalleventa, DetalleVenta))
        self.assertEqual(self.detalleventa.__str__(), "Detalle Venta Test")
    
    def test_detalleventa_fields(self):
        self.assertEqual(self.detalleventa.venta, "Venta Test")
        self.assertEqual(self.detalleventa.producto, "Producto Test")
        self.assertEqual(self.detalleventa.cantidad, 1)
        self.assertEqual(self.detalleventa.precio, 100.00)
        self.assertEqual(self.detalleventa.total, 100.00)

