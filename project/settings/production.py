from settings import * 

# Include all the settings specific to 'production' machines
# such as DATABASES, TIME_ZONE
DEBUG = False
DATABASES = {
    'default': {
        'NAME': 'geoplay_production',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'geoplay_production_user',
        'PASSWORD': '[set password here]',
        'HOST': 'localhost'
    }
}
