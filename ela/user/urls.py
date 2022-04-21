from django.urls import URLPattern, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

# 注意大小写要区分,不要过分依赖于补全!
urlpatterns = [
    # path('',views.index,name='index'),
    # as_view()注意小写V
    # path('', views.UserApiView.as_view(), name='userPost'),
    # path(r'^(?P<pk>)$',views.UserApiView.as_view(),name='userCheck'),
    # path(r'^user/$',views.UserApiView.as_view(),name='userCheck'),
    # path('userAdd/<str:name>', views.userAdd, name='userAdd'),
    # path('userCheck/<str:name>', views.userCheck, name='userCheck'),

    # re_path(r'^(?P<pk>\d+)/$', views.UserApiView.as_view()),
    re_path(r'^user/$',views.ListView.as_view()),
]

router = DefaultRouter()
# router=SimpleRouter()
# 简单路由
#
# router.register(r"user", views.UserApiViewSet)
# # 将DRF框架生成的连接插入到urlpatterns中
# urlpatterns += router.urls
# 通过启动项目,可以看到终端会打印出一系列的urlpatterns(routers.urls生成的)
# [
# <URLPattern '^user/$' [name='user-list']>,
# <URLPattern '^user/(?P<pk>[^/.]+)/$' [name='user-detail']>
# ]
# 譬如使用http://127.0.0.1:8000/user/user/来访问DRF提供的路由
print(urlpatterns)
