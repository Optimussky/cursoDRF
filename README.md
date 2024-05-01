
# Aprender a hacer un CRUD con Django Rest Framework
En este ejercicio intentaremos usar Python y Django para crear un API 

# cursoDRF
Curso Django - DRF (Django 5)

# Intalación de Django
	- pip install django==5

# Instalación de Django Rest Framework
	- URL = https://www.django-rest-framework.org/#installation
	- pip install djangorestframework

# Configuración de DRF en settings.py
	- 'rest_framework',

# Crear Repositorio en Github
	- cursoDRF

# Crear archivo .gitignore y agregar archivos y directorios
	Pipfile
	configura2.txt

# Hacer push en Github
	- git add .
	- git commit -m "Adding files"
	- git push

# Instalación de Postgres
	- pip install psycopg

# Crear base de datos en postgres
	- bd_inventario
	- puerto 5432
	- hacer desde terminal migrate
	- verificar en dbeaaver si ya existen las tablas de los modelos de django

# Crear nuestra API para crear nuestro Serializador
	- Nos permite convertir objetos de Django(Modelos) en un objeto JSON, para serializar y deserializar
	- Creamos una carpeta llamada api, nos posicionamos en nuestro proyecto "inventario" para crearla
	- Creamos nuestras clases para usar ModelViewsets para conseguir nuestro CRUD Generico
	- Creamos los archivos necesarios dentro de la carpeta api:
		- serializer.py
		- views.py
		- urls.py

