"""
Django settings for backEnd project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import datetime
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# from rest_framework.filters import OrderingFilter
# import word
# from word.filters import DIYPagination

BASE_DIR = Path(__file__).resolve().parent.parent
# 添加斜杠(对于put/post操作,url应该手动添加末尾的斜杠(下面的APPEND_SLASH=False则不会对末尾确实显式的`/`报错,但是这样不利于排查问题)
# APPEND_SLASH = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4@f$7t9t#zigdv1#5(&hd^oa!vetbizq*%#!%g@h71a_ir39@-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# 不可以再本文件(settings.py)中导入多余的包,容易造成某些配置无法正常工作!
# from  rest_framework.pagination import PageNumberPagination as PNP
# from django_filters.rest_framework import DjangoFilterBackend
# dpc="DEFAULT_PAGENATION_CLASS"


REST_FRAMEWORK = {
    # 权限认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  # 使用基本认证
        'rest_framework.authentication.SessionAuthentication',  # session认证
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 该jwt已经被废弃,无法在django版本中使用
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
    # 'DEFAULT_PERMISSON_CLASSES': (
    #     'rest_framework.permissions.AllowAny',
    # )
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 配置过滤
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],


    # 测试连接
    # 分页参数
    # http://127.0.0.1:8000/user/?page=2
    #  "next": "http://127.0.0.1:8000/user/?page=3",
    #  "previous": "http://127.0.0.1:8000/user/",
    # 分页配置:pagination
    # 分页方式1: limit&offset
    # 分页方式2:pager=x
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'word.paginations.DIYPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 3,  # each page content size
    # dpc:(PNP)
    # 在setting.Rest_Framework中注册自定义异常处理函数
    # 'EXCEPTION_HANDLER': 'my_project.my_app.utils.custom_exception_handler',
    # 获取路径的技巧:使用IDE搜索相应的类名/函数名(这里是函数名(符号),在顶一个该符号的地方右键复制其引用路径,既可以获得准确的符号访问路径!
    'EXCEPTION_HANDLER': 'backEnd.exceptions.division_exception_handler',
    # 接口文档配置(coreapi)
    # 注意还需要在urls.py中配置相应的url,否则无法访问!
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',

}
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}

# Application definition

INSTALLED_APPS = [
    # 提供点式路径
    # 以下点式路径由各自app目录下的apps.py中的class 提供
    # 在着就是注意各行必须以`,`结尾!
    # class UserConfig(AppConfig):
    #     default_auto_field = 'django.db.models.BigAutoField'
    #     name = 'user'
    # --------add your app to active (register) them!----------
    'drf_yasg',
    'coreapi',
    'django_filters',  # 过滤
    # django自带的过滤器主要面向前后端不分离
    # 采用drf的分页器,更好的支持前后你分离的项目
    # drf的分页器针对于ListView的功能(或者其子类的视图)才有效果!
    'rest_framework',  # DRF
    # 'blogs.apps.BlogsConfig',
    'main.apps.MainConfig',
    'scoreImprover.apps.ScoreImproverConfig',
    'word.apps.WordConfig',
    'user.apps.UserConfig',
    'django.contrib.admin',

    'polls.apps.PollsConfig',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #     注册自定义的中间件
    'user.loginMiddleware.LoginMiddleware',
]

# 当有请求到达,root_urlconf将会率先根据以下配置载入网站(backEnd)下的urls配置
# 先匹配(发来的请求url)到应用(譬如网站项目中的polls投票应用);
# 在将后面的细节参数传递给被匹配选中的应用内部的路由进行处理.
""" 当某人请求你网站的某一页面时——比如说， "/polls/34/" ，Django 将会载入 mysite.urls 模块，因为这在配置项 ROOT_URLCONF 中设置了。
然后 Django 寻找名为 urlpatterns 变量并且按序匹配正则表达式。在找到匹配项 'polls/'，它切掉了匹配的文本（"polls/"），
将剩余文本——"34/"，发送至 'polls.urls' URLconf 做进一步处理。在这里剩余文本匹配了 '<int:question_id>/'，
使得我们 Django 以如下形式调用 detail():
detail(request=<HttpRequest object>, question_id=34) 

"""
ROOT_URLCONF = 'backEnd.urls'

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

WSGI_APPLICATION = 'backEnd.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         # 'ENGINE':'django.db.backends.mysql',
#         # NAME:默认值 BASE_DIR / 'db.sqlite3' 将把数据库文件储存在项目的根目录(目录/数据库文件名)
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ela4',
        'USER': 'ela',
        'PASSWORD': '1',
        'HOST': '127.0.0.1',
        'PORT': '3306'
        # NAME:默认值 BASE_DIR / 'db.sqlite3' 将把数据库文件储存在项目的根目录(目录/数据库文件名)
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE':'django.db.backends.mysql',
    #     'NAME':'ela4',
    #     'USER':'ela',
    #     'PASSWORD':'1',
    #     'HOST':'123.56.72.67',
    #     'PORT':'3306'
    #     # NAME:默认值 BASE_DIR / 'db.sqlite3' 将把数据库文件储存在项目的根目录(目录/数据库文件名)
    #     # 'NAME': BASE_DIR / 'db.sqlite3',
    # }
}
if sys.argv[1] == 'test':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # DATABASES = {'default': 'psql://user:password@server:5432/database'}
    pass

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