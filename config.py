import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# BEGIN OAUTH

GOOGLE_LOGIN_CLIENT_ID = "<your-id-ending-with>.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "<your-secret>"

OAUTH_CREDENTIALS = {
    'google': {
        'id': GOOGLE_LOGIN_CLIENT_ID,
        'secret': GOOGLE_LOGIN_CLIENT_SECRET
    }
}
# END OAUTH
