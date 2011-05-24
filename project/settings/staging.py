from settings import * 

# Include all the settings specific to 'staging' machines
# such as DATABASES, TIME_ZONE, DEFAULT_FILE_STORAGE
DATABASES = {
    'default': {
        'NAME': 'geoplay_staging',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

