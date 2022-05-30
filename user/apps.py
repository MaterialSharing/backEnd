from django.apps import AppConfig

# 一下内容将注册在project/settings.py文件的installed 列表下
class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
