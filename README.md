# GestorDjango
práctica de django, realización de un gestor personal con agenda de contactos y función de búsqueda

la base de datos utilizada fue postgresSQL
como se especifica en los settings del proyecto

# Proyecto de Agenda con Django

Este proyecto es una aplicación de agenda desarrollada con Django y PostgreSQL. Sigue estos pasos para instalar, configurar y ejecutar el proyecto en tu entorno local.

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas:

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **pipenv** (gestor de entornos virtuales de Python)
- **PostgreSQL** (para la base de datos)

## Configuración de la Base de Datos

1. **Inicia sesión en PostgreSQL**:
   ```bash
   sudo -u postgres psql
2. **Inicia sesión en PostgreSQL**:
   ```sql 
   CREATE DATABASE agenda;
3. **Crea el usuario para la base de datos y otórgale permisos:**:
   ```sql 
   CREATE USER myproject_user WITH PASSWORD 'myproject_database_password';
   ALTER ROLE myproject_user SET client_encoding TO 'utf8';
   ALTER ROLE myproject_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE myproject_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE agenda TO myproject_user;

4. **Sal de PostgreSQL:**:
   ```sql    
   \q
## Instalación del Entorno Virtual y Dependencias

## Configuración del Entorno

1. **Clonar el repositorio**:
   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_repositorio>
2. **Crear el entorno virtual e instalar dependencias: Ejecuta el siguiente comando en la raíz del proyecto:**:
   ```bash 
   pipenv install
3. **Activa el entorno virtual:**:
   ```bash 
   pipenv shell
## Configuración del Proyecto Django

1. **Abre el archivo agenda/settings.py y asegúrate de que la configuración de la base de datos sea la siguiente:**:
   ```python
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "agenda",
        "USER": "myproject_user",
        "PASSWORD": "myproject_database_password",
        "HOST": "localhost",
        "PORT": "",
        }
    }
    ```

## Migración de la Base de Datos
**Aplica las migraciones para configurar la base de datos:**:
   ```bash 
   pipenv run python manage.py migrate
```
## Ejecución del Servidor de Desarrollo
**Inicia el servidor de desarrollo de Django:**:
   ```bash 
   pipenv run python manage.py runserver
