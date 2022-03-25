"""
프로젝트에 대한 비동기 서버게이트웨이 인터페이스(ASGI: Asynchorous Server Gateway Interface) 설정 파일.

참고) https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.local')

application = get_asgi_application()
