# EMAIL_HOST_USER = 'medidorinteligente25@gmail.com'
# EMAIL_HOST_PASSWORD = "zdxf thzc lauz kmxd"
# EMAIL_HOST_PASSWORD = secret_key = os.getenv("SECRET_KEY")


# Configuración de EMAIL_HOST_PASSWORD con SECRET_KEY en Django

Este documento explica cómo configurar `EMAIL_HOST_PASSWORD` utilizando `SECRET_KEY` en un proyecto Django, asegurando que la clave se almacene de manera segura mediante variables de entorno o un archivo `.env`.

## 1. Definir la variable de entorno

Antes de acceder a `SECRET_KEY` en el código, asegúrate de definirla en el entorno del sistema o en un archivo de configuración.

### En Linux/macOS (Terminal o en `.bashrc`, `.zshrc`):
```bash
export SECRET_KEY="tu_clave_secreta_aqui"
```

### En Windows (cmd):
```cmd
set SECRET_KEY=tu_clave_secreta_aqui
```

### En Windows (PowerShell):
```powershell
$env:SECRET_KEY="tu_clave_secreta_aqui"
```

## 2. Usar un archivo `.env` (opcional, recomendado)
Si prefieres gestionar las variables de entorno en un archivo, usa `.env` y la librería `dotenv`:

### Instalar `dotenv`:
```bash
pip install python-dotenv
```

### Crear un archivo `.env` en la raíz del proyecto:
```
SECRET_KEY=tu_clave_secreta_aqui
```

### Modificar `settings.py` para cargar las variables de entorno:
```python
from dotenv import load_dotenv
import os

load_dotenv()  # Cargar variables desde .env

secret_key = os.getenv("SECRET_KEY")
EMAIL_HOST_PASSWORD = secret_key
```

## 3. Verificar que la variable está cargada correctamente
Para asegurarte de que la variable se está recuperando bien, imprime su valor temporalmente en el código:
```python
print(f"SECRET_KEY: {secret_key}")  # No hacer esto en producción
```
Si el valor es `None`, significa que la variable no está definida correctamente en el entorno.

## 4. Configuración del correo en Django
Si estás configurando el correo en Django, asegúrate de definir los siguientes ajustes en `settings.py`:
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.tudominio.com"  # Ejemplo: smtp.gmail.com
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "tu_email@dominio.com"
EMAIL_HOST_PASSWORD = os.getenv("SECRET_KEY")  # Usando la variable de entorno
```

## 5. Posibles Problemas y Soluciones
### `None` o cadena vacía en `SECRET_KEY`
- Asegúrate de que la variable está realmente definida en el entorno antes de ejecutar el servidor.
- Si usas `.env`, revisa que `load_dotenv()` se ejecuta antes de llamar `os.getenv("SECRET_KEY")`.

### `EMAIL_HOST_PASSWORD` no funciona
- Algunos servicios de correo (como Gmail) requieren que uses una **contraseña de aplicación** en lugar de la contraseña normal.
- Verifica que el servicio de correo que usas acepta autenticación con contraseña y que `EMAIL_USE_TLS` o `EMAIL_USE_SSL` estén configurados correctamente.

## Conclusión
- Define `SECRET_KEY` en el entorno o usa un archivo `.env`.
- Usa `os.getenv("SECRET_KEY")` para obtener el valor.
- Verifica que la variable está cargada correctamente.
- Si es para correo en Django, revisa la configuración SMTP.



