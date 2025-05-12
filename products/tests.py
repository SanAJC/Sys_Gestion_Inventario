from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from decimal import Decimal
from .models import Producto, Proveedor


class ProveedorModelTest(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor Test",
            telefono="123456789",
            email="proveedor@test.com",
            direccion="Calle Test 123"
        )
    
    def test_proveedor_creation(self):
        self.assertTrue(isinstance(self.proveedor, Proveedor))
        self.assertEqual(self.proveedor.__str__(), "Proveedor Test")
    
    def test_proveedor_fields(self):
        self.assertEqual(self.proveedor.nombre, "Proveedor Test")
        self.assertEqual(self.proveedor.telefono, "123456789")
        self.assertEqual(self.proveedor.email, "proveedor@test.com")
        self.assertEqual(self.proveedor.direccion, "Calle Test 123")


class ProductoModelTest(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor Test",
            telefono="123456789",
            email="proveedor@test.com",
            direccion="Calle Test 123"
        )
        
        self.producto = Producto.objects.create(
            nombre="Producto Test",
            precio=Decimal('99.99'),
            stock=10,
            proveedor=self.proveedor
        )
    
    def test_producto_creation(self):
        self.assertTrue(isinstance(self.producto, Producto))
        self.assertEqual(self.producto.__str__(), "Producto Test")
    
    def test_producto_fields(self):
        self.assertEqual(self.producto.nombre, "Producto Test")
        self.assertEqual(self.producto.precio, Decimal('99.99'))
        self.assertEqual(self.producto.stock, 10)
        self.assertEqual(self.producto.img.name, None) 
    
    def test_producto_proveedor_relation(self):
        self.assertEqual(self.producto.proveedor, self.proveedor)
        self.assertEqual(self.producto.proveedor.nombre, "Proveedor Test")


class ProductoConImagenTest(TestCase):
    
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre="Proveedor Test",
            telefono="123456789",
            email="proveedor@test.com",
            direccion="Calle Test 123"
        )
    
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'', 
            content_type='image/jpeg'
        )
        
        self.producto = Producto.objects.create(
            nombre="Producto Con Imagen",
            precio=Decimal('149.99'),
            img=self.image,
            stock=5,
            proveedor=self.proveedor
        )
    
    def test_producto_con_imagen(self):
        self.assertTrue(isinstance(self.producto, Producto))
        self.assertIsNotNone(self.producto.img)
        self.assertTrue(self.producto.img.name.startswith('products/'))
