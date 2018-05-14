from .base import *
DEBUG=True
MEDIA_URL='/media/'
MEDIA_ROOT='media'

STATIC_URL = '/static/'
STATIC_ROOT='staticfiles'

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.environ["SENDGRID_API_KEY"]