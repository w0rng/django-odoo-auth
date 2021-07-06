import xmlrpc.client

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from . import settings


class OdooBackend(BaseBackend):
    def __init__(self):
        url_login = f'{settings.ODOO_SERVER_URL}:{settings.ODOO_SERVER_PORT}/xmlrpc/2/common'
        self.ODOO_SOCK_COMMON = xmlrpc.client.ServerProxy(url_login)

    def authenticate(self, request, username=None, password=None):
        user_uid = self.ODOO_SOCK_COMMON.authenticate(
            settings.ODOO_SERVER_DBNAME,
            username,
            password,
            {},
        )
        if user_uid is None:
            return None
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            return user
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
