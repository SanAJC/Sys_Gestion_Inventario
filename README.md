# Sys_Gestion_Inventario

Aplicación web para la gestión integral de inventarios, permitiendo a los usuarios administrar productos, clientes y ventas de manera eficiente a través del panel de administración de Django.

## 🚀 Tecnologías Utilizadas

- **Backend:**
  - [Python](https://www.python.org/): Lenguaje de programación utilizado para el desarrollo del backend.
  - [Django](https://www.djangoproject.com/): Framework web de alto nivel que fomenta el desarrollo rápido y limpio.

- **Base de Datos:**
  - [SQLite](https://www.sqlite.org/index.html): Base de datos ligera utilizada por defecto en Django para desarrollo.

- **CI/CD:**
  - [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/): Plataforma utilizada para la integración y entrega continuas mediante pipelines definidos en YAML.

## 📂 Estructura del Proyecto

```bash
Sys_Gestion_Inventario/
├── clientes/
├── gestion_inventario/
├── media/
│ └── products/
├── products/
├── ventas/
├── manage.py
├── requirements.txt
├── azure-pipelines.yml
└── README.md
```
## 🧩 Funcionalidades

- **Gestión de Productos:** Crear, editar y eliminar productos, incluyendo detalles como nombre, descripción, precio y stock.
- **Gestión de Clientes:** Registrar y administrar información de clientes.
- **Gestión de Ventas:** Registrar ventas, asociar productos y clientes, y generar reportes de ventas.
- **Carga de Imágenes:** Subir y visualizar imágenes de productos.
- **Autenticación de Usuarios:** Registro e inicio de sesión seguros para proteger la información.
- **Panel de Administración:** Interfaz proporcionada por Django para la gestión eficiente de los datos.

## 🔧 Instalación y Ejecución

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/SanAJC/Sys_Gestion_Inventario.git
   cd Sys_Gestion_Inventario
