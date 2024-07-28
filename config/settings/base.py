"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# BASE_DIR = Path(__file__).resolve().parent.parent 파일을 나누면서 한 단계 더 상위 디렉터리로 이동


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d@twn1l-fsr54oi+_l*gkyupd=mrm^tl+vyrdtc(y$@ehtft#h' # 임시로 변경

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # 개발 단계에서는 True로 설정

ALLOWED_HOSTS = ['3.37.225.147'] # 서버의 IP 주소를 추가


# Application definition

INSTALLED_APPS = [
    'common.apps.CommonConfig', # common 애플리케이션 추가
    'pybo.apps.PyboConfig', # pybo 애플리케이션 추가
    'django.contrib.admin', # 관리자 사이트
    'django.contrib.auth', # 로그인, 로그아웃 기능
    'django.contrib.contenttypes', # 컨텐츠 타입 관리
    'django.contrib.sessions', # 세션 관리
    'django.contrib.messages', # 메시지 프레임워크
    'django.contrib.staticfiles', # 정적 파일 관리
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # 보안 관련 중간관리자
    'django.contrib.sessions.middleware.SessionMiddleware', # 세션 관리
    'django.middleware.common.CommonMiddleware', # 기본 요청/응답 처리
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF 보호 관리
    'django.contrib.auth.middleware.AuthenticationMiddleware', # 사용자 인증
    'django.contrib.messages.middleware.MessageMiddleware', # 메시지 프레임워크
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # 클릭재킹 방어
]

ROOT_URLCONF = 'config.urls' # URL 매핑 파일

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # 템플릿 엔진
        'DIRS': [BASE_DIR / 'templates'], # 템플릿 파일의 위치
        'APP_DIRS': True, # 애플리케이션별 템플릿 사용 여부
        'OPTIONS': { # 추가 옵션
            'context_processors': [ # 템플릿 전역 변수 설정
                'django.template.context_processors.debug', # 디버그 정보
                'django.template.context_processors.request', # HttpRequest 객체
                'django.contrib.auth.context_processors.auth', # 로그인 관련 정보
                'django.contrib.messages.context_processors.messages', # 메시지 프레임워크
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application' # WSGI 애플리케이션


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = { # 데이터베이스 설정
    'default': { # 기본 데이터베이스
        'ENGINE': 'django.db.backends.sqlite3', # SQLite3 사용
        'NAME': BASE_DIR / 'db.sqlite3', # 데이터베이스 파일 경로
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 로그인 URL
LOGIN_REDIRECT_URL = '/'

# 로깅설정
# 로깅설정
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            #'format': '[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] [%(module)s:%(funcName)s] %(message)s'
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/ksham.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'pybo': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}