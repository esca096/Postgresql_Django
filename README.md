
Installer les dépendances nécessaires
1- Assurez-vous d'abord d'avoir PostgreSQL installé sur votre machine.


2- Installez le package Python psycopg2 qui permet à Django de communiquer avec PostgreSQL :
# pip install psycopg2-binary


3- Installez django-environ pour gérer les variables d'environnement :
# pip install django-environ


4- Importez environ en haut de votre fichier settings.py :
# import environ


5- Initialisez environ et lisez le fichier .env  dans settings.py:

****

# env = environ.Env(
    # définir des valeurs par défaut pour les variables d'environnement
    DEBUG=(bool, False)
)

# Lire le fichier .env
environ.Env.read_env()

****


6- Configurez votre base de données dans settings.py :

***

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

***



7- Exemple complet de settings.py


8- Créez un fichier .env à la racine de votre projet (au même niveau que manage.py) et ajoutez vos identifiants de base de données :

*** 

SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

***



9- Effectuer les migrations vers la base de donnée postgresql

