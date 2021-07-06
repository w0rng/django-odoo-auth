from django.conf import settings


ODOO_SERVER_URL = getattr(settings, 'ODOO_SERVER_URL', 'http://localhost')
ODOO_SERVER_PORT = getattr(settings, 'ODOO_SERVER_PORT', 80)
ODOO_SERVER_DBNAME = getattr(settings, 'ODOO_SERVER_DBNAME', 'demo')
