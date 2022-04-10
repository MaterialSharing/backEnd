
from django.urls import URLPattern, path,re_path
from . import views
# 注意大小写要区分,不要过分依赖于补全!
urlpatterns=[
    path('',views.index,name='index'),
    path('userAdd/<str:name>',views.userAdd,name='userAdd'),
    path('userCheck/<str:name>',views.userCheck,name='userCheck')
]