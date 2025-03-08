**Documentación del Proyecto: Medidor Inteligente**

## 1. Introducción
Medidor Inteligente es una aplicación desarrollada en Django que permite enviar información al usuario, facilitar ventas y brindar información relevante sobre el consumo de agua potable.

## 2. Instalación y Configuración

### Requisitos previos
Antes de instalar el proyecto, asegúrese de contar con:
- **Python** (Descargar desde [python.org](https://www.python.org/))
- **Git**
- **Virtualenv**
- **Visual Studio Code** (Descargar desde [code.visualstudio.com](https://code.visualstudio.com/))
- **Extensiones de Visual Studio Code**:
  - Django
  - GitHub
  - Git
  - IntelliCode
  - Live Server
  - Live Share
  - Python
  - Python Debugger
  - Remote Repositories
  - SQLite
  - VSCode-PDF


### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/LisaRamirez/Medidor-Inteligente.git
   cd Medidor-Inteligente
   ```

2. **Crear y activar un entorno virtual**
   ```bash
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate  # (En Windows: venv\Scripts\activate)
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos** (SQLite se genera automáticamente)
   ```bash
   python manage.py migrate
   ```

5. **Crear un superusuario para acceder al panel de administración**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```
   Acceda a `http://127.0.0.1:8000/` en su navegador.

## 3. Estructura del Proyecto
El proyecto sigue la estructura estándar de Django:
```
/Medidor-Inteligente/
├── app/
│ ├── pycache/
│ ├── migrations/
│ ├── static/
│ │ ├── app/
│ │ ├── css/
│ │ ├── img/ja
│ │ 
│ ├── templates/
│ │ ├── app/
│ │ ├── apr.html
│ │ ├── base.html
│ │ ├── clientes.html
│ │ ├── contacto.html
│ │ ├── e404.html
│ │ ├── home.html
│ │ ├── nosotros.html
│ │ ├── prueba.html
│ │ ├── recursos.html
│ │ └── soluciones.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── apr/
├── media/
├── medidor/
├── pycache/
├── init.py
├── asgi.py
├── settings.py
├── urls.py
├── wsgi.py
├── db.sqlite3
├── debug.log
├── manage.py
└── requirements.txt```


### Descripción de Carpetas y Archivos

- **app/**: Contiene la aplicación principal del proyecto.
  - **migrations/**: Almacena las migraciones de la base de datos.
  - **static/**: Contiene archivos estáticos como CSS, imágenes y JavaScript.
    - **css/**: Archivos de estilos CSS.
    - **img/**: Imágenes utilizadas en el proyecto.
    - **js/**: Archivos JavaScript para la interactividad.
  - **templates/**: Plantillas HTML para las diferentes vistas de la aplicación.
    - **app/**: Plantillas específicas de la aplicación.
    - **base.html**: Plantilla base para otras plantillas.
    - **home.html**: Página de inicio.
    - **clientes.html**: Página de clientes.
    - **contacto.html**: Página de contacto.
    - **nosotros.html**: Página "Nosotros".
    - **soluciones.html**: Página de soluciones.
    - **recursos.html**: Página de recursos.
    - **e404.html**: Página de error 404.
    - **prueba.html**: Página de prueba.
    - **apr.html**: Página específica para APR (Asociaciones de Agua Potable Rural).
  - **models.py**: Define los modelos de la base de datos.
  - **views.py**: Contiene las vistas (lógica de la aplicación).
  - **urls.py**: Define las rutas URL de la aplicación.
  - **forms.py**: Contiene formularios para la aplicación.
  - **admin.py**: Configuración del panel de administración de Django.
  - **tests.py**: Pruebas unitarias para la aplicación.

- **apr/**: Carpeta relacionada con las Asociaciones de Agua Potable Rural (APR).
- **media/**: Almacena archivos multimedia subidos por los usuarios.
- **medidor/**: Contiene archivos relacionados con los medidores inteligentes.
- **settings.py**: Configuración del proyecto Django.
- **urls.py**: Rutas URL principales del proyecto.
- **db.sqlite3**: Base de datos SQLite utilizada en desarrollo.
- **manage.py**: Script para gestionar el proyecto Django.
- **requirements.txt**: Lista de dependencias del proyecto.

Para ejecutar este proyecto, necesitas tener instalado Python y las dependencias listadas en `requirements.txt`. Puedes instalarlas usando el siguiente comando:

```bash
pip install -r requirements.txt

## 4. Uso y Funcionalidades
- **Visualización de datos del medidor**.
- **Gestión de usuarios y acceso**.
- **Panel de administración Django** (`/admin`).

## 5. Seguridad y Buenas Prácticas
- **Usar variables de entorno** para credenciales (`.env`).

## 6. Recursos Adicionales
- [Documentación oficial de Django](https://docs.djangoproject.com/en/stable/)

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

Creado por WamDigital.cl
