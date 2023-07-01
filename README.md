# Nombre del Proyecto

Esta aplicacion es el backend para la app de pedidos

## Requisitos previos

Asegúrate de tener instalado lo siguiente en tu entorno de desarrollo:

- Python (versión 3.11.3)

## Configuración del entorno

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/williamdaza01/pedidosapp.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd pedidosapp/
   cd pedidosBack/
   ```

3. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

4. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

5. Configura la base de datos:

   - Abre el archivo `settings.py`
   - Actualiza las configuraciones de la base de datos según tus preferencias (por ejemplo, nombre de la base de datos, usuario, contraseña, etc.).

6. Realiza las migraciones:

   ```bash
   python manage.py migrate
   ```

## Ejecución del proyecto

Para ejecutar el proyecto de Django, sigue estos pasos:

1. Activa el entorno virtual si aún no lo has hecho:

   ```bash
   source venv/Scripts/activate
   ```

2. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

3. Abre tu navegador web y accede a la siguiente URL:

   ```
   http://localhost:8000/
   ```

¡Ahora deberías ver el proyecto de Django en ejecución en tu navegador!

