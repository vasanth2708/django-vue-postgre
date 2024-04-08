Setup environment - 
- Install python3.9 version using link - https://www.python.org/downloads/release/python-3913/
- python3.9 -m venv myenv
- source myenv/bin/activate
- pip install django
- pip install djangorestframework
- npm install -g @vue/cli
- npm install axios
- pip install django-cors-headers
- pip install stripe
- pip install djoser
- pip install --upgrade pip setuptools wheel
- pip install Pillow
- brew install jpeg libpng libtiff

Update the postgre sql details in settings.py - 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '', 
        'USER': '',
        'PASSWORD': '',
        'HOST': '', 
        'PORT': '',
    }
}


Executation Navigate to myEcom folder- 
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

Navigate to ecom_vue -
setup env - export NODE_OPTIONS=--openssl-legacy-provider
Execution Vue - 
- npm install
- npm run serve


