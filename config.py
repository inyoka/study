
'''
from private import GOOGLE_LOGIN_CLIENT_ID, GOOGLE_LOGIN_CLIENT_SECRET
from private import TWITTER_LOGIN_CLIENT_ID, TWITTER_LOGIN_CLIENT_SECRET
from private import FACEBOOK_LOGIN_CLIENT_ID, FACEBOOK_LOGIN_CLIENT_SECRET
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['simonmarkholland@gmail.com']


OAUTH_CREDENTIALS = {
    'google': {
        'id': GOOGLE_LOGIN_CLIENT_ID,
        'secret': GOOGLE_LOGIN_CLIENT_SECRET
    },
    'twitter': {
        'id': TWITTER_LOGIN_CLIENT_ID,
        'secret': TWITTER_LOGIN_CLIENT_SECRET
    },
    'facebook': {
        'id': FACEBOOK_LOGIN_CLIENT_ID,
        'secret': FACEBOOK_LOGIN_CLIENT_SECRET
    }
}
'''
