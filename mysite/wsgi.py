"""
프로젝트 웹서버게이트웨이 인터페이스(WSGI: Web Server Gateway Interafce)

참고) https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')

application = get_wsgi_application()
