class secrets():

    key = 'KEY'

    db_config = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'statusConsole',
            'USER': 'DATABASE USER',
            'PASSWORD': 'DATABASE PASSWORD',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


    smtp_pass = 'EMAIL PASSWORD'
