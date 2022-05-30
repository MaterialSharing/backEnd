from django.apps import AppConfig

# 类名可以作为应用点事路径中的末尾部分.(在project/settings.installed_app数组中配置.)
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
