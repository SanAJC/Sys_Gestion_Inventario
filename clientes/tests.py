from django.test import TestCase
from .models import Cliente

class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nombre="Cliente",
            apellido="Test",
            telefono="123456789",
            email="cliente@test.com",
            direccion="Calle Test 123"
        )
    
    def test_cliente_creation(self):
        self.assertTrue(isinstance(self.cliente, Cliente))
        self.assertEqual(self.cliente.__str__(), "Cliente Test")
    
    def test_cliente_fields(self):
        self.assertEqual(self.cliente.nombre, "Cliente")
        self.assertEqual(self.cliente.apellido, "Test")
        self.assertEqual(self.cliente.telefono, "123456789")
        self.assertEqual(self.cliente.email, "cliente@test.com")
        self.assertEqual(self.cliente.direccion, "Calle Test 123")

