from django.urls import URLPattern, path, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views

'''
低级错误检测
# 注意大小写要区分,不要过分依赖于补全!
# as_view()注意小写V
'''
# 原生开发api(不采用通用视图,只采用函数直接定义路由到视图函数)
'''
urlpatterns=[
    # path('',views.index,name='index'),
    # path('user/', views.userAdd, name='userAdd'),#post a new user entry to the database
    # path('user/', views.userAdd, name='userAdd'),#get all user entry to the database
    # path('user/<str:name>', views.userCheck, name='userCheck'),# get a user entry from database 
]
 
'''
# 原生开发api(基于通用视图集)所配置的路由:
urlpatterns = [
    path('', views.UserView.as_view(), name='userPost'),
    # regex array without regexp
    # re_path(r'^(?P<pk>)$',views.UserApiView.as_view(),name='userCheck'),
    re_path(r'^user/$', views.UserView.as_view(), name='userCheck'),
    re_path(r'^(?P<pk>\d+)/$', views.UserView.as_view(), name='userCheck'),

]
# 废弃原生开发
urlpatterns = []

# 采用drf方式配置路由
# urlpatterns = [
#     re_path(r'^user/$',views.ListView.as_view()),
# ]

router = DefaultRouter()
# router.register("user", views.UserApiViewSet, basename="user"),
'''
def register(self,

             prefix: Any,
             viewset: Any,
             basename: Any = None
             ) -> None
 '''
# 最终版本路由(预览)
router.register("user_d", views.UserApiViewSet, basename="user_drf"),
urlpatterns = [] + router.urls
# 暂时关闭
urlpatterns = []
# 使用drf逐级改造
urlpatterns = [
    # user应用内的子路由配置
    # 这里的user表示'资源'(总路由中的user表示应用名)
    path('user/', views.UserSerView.as_view()),
    path('user_apiView/', views.UserAPIView.as_view()),
    re_path('^user_apiView/(?P<pk>\d+)$', views.UserInfoAPIView.as_view()),
    re_path('^user_generic/(?P<pk>\d+)$', views.UserInfoGenericAPIView.as_view()),
    re_path('^user_generic/$', views.UserGenericAPIView.as_view()),
    re_path('^user_genericMixin/$', views.UserGenericMixin.as_view()),
    re_path('^user_genericMixin/(?P<pk>\d+)$', views.UserInfoGenericMixin.as_view()),
]

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
