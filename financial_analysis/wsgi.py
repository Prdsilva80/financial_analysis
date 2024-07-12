# financial_analysis/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financial_analysis.settings')

application = get_wsgi_application()
