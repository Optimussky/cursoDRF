
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

# Proteger API en Django Rest Framework con JWT
	- instalación de modulo:
		pip install djangorestframework-simplejwt
	
	*.  ESTRUCTURA DE UN JSON WEB TOKEN (JWT)
	- HEADER : "algoritmo": "HS256"
	- PAYLOAD: DATA ({"nom": "Juan", "edad": 30, "estatus": "activo"})
	- SIGNATURE: Firma validada de nuestro Token

	- URL para probar JWT: jwt.io

# Configuración del Proyecto:

	- Agregar en settings.py en el apartado de INSTALED_APPS, lo siguiente:
	
		INSTALLED_APPS = [
			'rest_framework_simplejwt',
		]
	



	- Agregar al archivo settings.py en la lista de clases de autenticación:


	REST_FRAMEWORK = {
		
		'DEFAULT_AUTHENTICATION_CLASSES' :(
		
		'rest_framework_simplejwt.authentication.JWTAuthentication',
		)
	}
	

	- Además en la raíz en urls.py, incluir rutas para Simple JWT:

	

	from rest_framework_simplejwt.views import (
		TokenObtainPairView,
		TokenRefreshView,
	)

	urlpatterns = [
		path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
		path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
	]


# Comprobar que no hay errores
	python manage.py runserver 8500

	* Es necesario contar con un usuario para hacer pruebas por lo que vamos a crear uno desde terminal

	python manage.py createsuperuser

# Hacemos una prueba desde POSTMAN a la URL
	http://127.0.0.1/api/token/

	Haciendo uso del Método POST
	El resultado es que es requerido un user y pass
	por lo 	que en POSTMAN podemos pasarle un JSON
	
	{
		"user":"Beto",
		"password","12345"
	}
	

	Mismo que nos regresará una cadena de texto con nuestro token con dos parámetros
	
	{

		"access": "456789oksjnaL",
		"refresh": "lkjhg9876h"
	}


# Agregar permisos a las vistas
	- vamos a nuestra App (startapp) y en el archivo inventario/api/views.py agregamos dentro de nuestra clase el siguiente codigo:

	
	from rest_framework.permission import IsAtuthenticated

	permission_classes = [IsAuthenticated] # Agregamos una lista para permisos

	
	- Para comprobar que esta funcionando revisamos nuevamente nuestra URL hhtp://localhost:8500/api/productos/ con el Método GET

	Y el resultado debería ser:
	
	{
		"detail" : "Authentication credentials wre not provided."
	}
	

# También podemos pedir token a todas las api's ( para configurarlo vamos a nuestro archivo settings.py)
```
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework_simplejwt.authentication.JWTAuthentication',
	),
	# Pedir token en todas las api's
	'DEFAULT_PERMISSION_CLASSES': {
		'rest_framework.permissions.IsAuthenticated', # Con esto pedimos tokens para todas las apis
	},
}

```

## VAMOS A UTILIZAR EL TOKEN QUE HEMOS CREADO


```
En la ruta HACEMOS un POST:
http://localhost:8500/api/token/

Usamos el access token EN http://localhost:8500/api/productos Hacemos un GET
Y lo colocamos en:
	- Authorization
	- Bearer Token
	- Pegamos el access token para hacer nuestra solicitud GET


```

## CUSTOMIZANDO EL TIEMPO DE VIDA DE LOS JWT
	- Dentro de nuestro archivo settings.py podemos hacer algunas modificaciones como lo muestra la URL:
	https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

	# Django project settings.py

from datetime import timedelta
...

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}



