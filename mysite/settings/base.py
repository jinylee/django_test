"""
프로젝트 Django 설정 파일
아래와 같은 명령으로 자동생성할 수 있음
$> django-admin startproject 프로젝트명

참고) https://docs.djangoproject.com/en/4.0/topics/settings/
참고) https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import os

# 프로젝트 기본 경로.ex) parent.parent => ..

BASE_DIR = Path(__file__).parent.parent.parent

# 상용인 경우 아래의 링크 참고하여 설정해야함
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# ----------------------------------------------------------------------------------------------------------------------
# 환경변수 획득하여 글로벌 설정
# ----------------------------------------------------------------------------------------------------------------------
SERVER_ENV = os.environ.get('SERVER_ENV', 'local')

# ----------------------------------------------------------------------------------------------------------------------
# Django 기본설정
# ----------------------------------------------------------------------------------------------------------------------
# 상용인 경우, 별도 환결설정으로 받아야 와야함
# SECURITY WARNING
SECRET_KEY = 'django-insecure-z)wn5=29qyqc2l=@dt(se=ib47jou0$d6c-n-wc2!zn=48w6s0'
## 상용. compose/.env 등을 통해 주입받도록 하자.
#SECRET_KEY = os.environ.get('TESTWAS_SECRET_KEY')

# SECURITY WARNING
DEBUG = True

# 하용할 호스트 리스트
ALLOWED_HOSTS = ['*']

# CSRF(Cross Site Request Forgery) 쿠키 보안
# 방어정책으로 referrer 검증, CSRF Token 검증 (Session, Cookie)
CSRF_COOKIE_SECURE = False

# 어플리케이션 정의
INSTALLED_APPS = [
    'django.contrib.admin',             # 관리용 사이트 - 삭제필요
    'django.contrib.auth',              # 인증 시스템 - 사용
    'django.contrib.contenttypes',      # 컨텐츠타입 프레임워크 - 사용
    'django.contrib.sessions',          # 세션 프레임워크 -  사용
    'django.contrib.messages',          # 메시징 프레임워크 - 선택
    'django.contrib.staticfiles',       # 정적파일 관리 프레임워크 - 사용
    'polls.apps.PollsConfig'            # polls/apps.py#PollsConfig App 설정 파일
]
# 요청/응답 처리 관련 프레임워크. 입력/출력을 전체적으로 변경하기 위한 경량 플러그인
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Proxy 'mysite/urls.py' 참조
ROOT_URLCONF = 'mysite.urls'

# 템플릿 파일(html) 검색 경로
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 실행 함수. mysite/wsgi.py#application
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
