from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

# 由于我中途将这个模块拆分出来，所以这里的view要小心导入
# import user.views.User
# from . import views

# from .views import WSHModelViewSet
import user
from user import views
from user.views import star
from user.views.history import WSHModelViewSet
from user.views.login import Login
from user.views.star import WordStarModelViewSet
from user.views.user import UserModelViewSet, UserRegisterModelViewSet
from user.views.user_basic import UserView

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
    path('', UserView.as_view(), name='userPost'),
    # regex array without regexp
    # re_path(r'^(?P<pk>)$',views.UserApiView.as_view(),name='userCheck'),
    re_path(r'^user/$', UserView.as_view(), name='userCheck'),
    re_path(r'^(?P<pk>\d+)/$', UserView.as_view(), name='userCheck'),
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
# router.register("user_d", views.UserApiViewSet, basename="user_drf"),
urlpatterns = [] + router.urls
# 暂时关闭
urlpatterns = []
# 使用drf逐级改造
urlpatterns = [
    # user应用内的子路由配置
    # 这里的user表示'资源'(总路由中的user表示应用名)
    # path('user/', views.UserSerView.as_view()),
    # path('user_apiView/', views.UserAPIView.as_view()),
    # re_path('^user_apiView/(?P<pk>\d+)$', views.UserInfoAPIView.as_view()),
    # re_path('^user_generic/(?P<pk>\d+)$', views.UserInfoGenericAPIView.as_view()),
    # re_path('^user_generic/$', views.UserGenericAPIView.as_view()),
    # re_path('^user_genericMixin/$', views.UserGenericMixin.as_view()),
    # re_path('^user_genericMixin/(?P<pk>\d+)$', views.UserInfoGenericMixin.as_view()),
    # re_path('user_ListCreate/', views.UserListCreateAPIView.as_view()),
    # re_path('^user_RetrieveUpdate/(?P<pk>\d+)$', views.UserRetrieveUpdateAPIView.as_view()),
    # re_path('^user_RetrieveUpdateDestroy/(?P<pk>\d+)$', views.UserRetrieveUpdateDestroyAPIView.as_view()),
    path('info/<int:pk>/signin/', UserModelViewSet.as_view({
        "put": "signin"
    }), name='signin'),
    # path('info/<int:pk>/review/<str:examtype>/list',
    # 注意re_path不支持类型转换器(<int:pk>)这类写法在re_path中会失效,导致无法正确解析路由
    # 不要混用正则和类型转换器!
    re_path('^info/(?P<pk>\d+)/review/global/(?P<examtype>\w+)/$',
            UserModelViewSet.as_view({
                "get": "review_list"
            }),
            name="review-list"
            ),
    # 小心不要被前面的类似路由所覆盖,这样是没有机会访问到为与后面的路由.
    path('info/<int:pk>/review/recently/',
         UserModelViewSet.as_view({'get': 'recently_unitable'}),
         name='review_recently'),
    # path('info/<int:pk>/review/', views.UserModelViewSet.as_view({
    #     "get": "review"
    # })),
    # re_path('^info/(?P<pk>\d+)/review/(?P<unit>\w+)/(?P<value>(\-|\+)?\d+(\.\d+)?)/$',
    #         views.UserModelViewSet.as_view({'get': 'recently_unitable'})),
    path('info/<int:pk>/rank/', UserModelViewSet.as_view({
        "get": "rank"
    }), name="rank"),
    path('info/<int:pk>/progress/<str:examtype>/',
         UserModelViewSet.as_view({
             "get": "progress"
         }),
         name="progress"),
    path('info/<int:pk>/schedule/', UserModelViewSet.as_view({
        "get": "schedule"
    }), name="schedule"),
    path('login/', Login.as_view({
        "get": "login"
    }), name="login"),
    path('dologin/', Login.as_view({
        "post": "dologin"
    }), name="dologin"),
    path('logout/', Login.as_view({
        "delete": "logout"
    }), name="logout"),
    path('fetch-user/', Login.as_view({
        "get": "fetch_user"
    }), name="fetch_user"),
    path('user/timer-days/', UserModelViewSet.as_view({"get": "timer_days"}))

    # path('info/<int:pk>/review/<str:examtype>/recently/<str:unit>/<str:value>',
    #      views.UserModelViewSet.as_view({'get': 'recently_unitable'})),
    # path('info/<int:pk>/history/', views.WSHModelViewSet.as_view())

]
# 多对多(user_word_star)
# post 不应该将参数放置在url中:'<int:uid>/star/<str:word>/' bad behaviour!
# path('star/', views.WordStarModelViewSet.as_view(
#     {
#         'post': 'star_word'
#     }
# )),
# path('history/', WSHModelViewSet.as_view({
#     'post': 'history_create'
# }))

# 1 添加自定视图函数(尤其是在基本的CRUD操作之外的操作.有多种方案
# 2 采用视图集
# 3  视图图集可以通过DRF提供的as.views()函数,通过传入映射http动作:自定函数的映射关系子字典,来区分和调用不同的处理函数
# 3 一个视图集中可以有多个隶属于get动作的方法,但是为例区分它们,你需要编写相应数量的路由(以及指定映射关系使得自定函数能够工作)
# 2 采用api分散在多个视图类中的方式编写多个方法,视图类中的方法名局限于与固定的几个方法名,可以通过注释来加说明函数/参数用途
# 3 比如前面的get(无参)获取全部数据的方法,以及需要指定主键pk的get方法,将它们放置在不同的视图类中
# 3这种方式,也是通过编写路由来区分函数调用(

# ViewSet series:(两种匹配模式共用统一一个视图类
# 视图集(ViewSet)使得路由的代码变得冗长,后期可以使用默认路由来配合ViewSet的路由简化给部分的编写

# path('user_ViewSet/', views.UserViewSet.as_view({
#     "get": "get_all",
#     "post": "post"
# })),
# re_path('^user_ViewSet/(?P<pk>\d+)$', views.UserViewSet.as_view({
#     "get": "get_info",
#     "put": "update"
# })),
# # GenericViewSet(注意,以下的映射需要以默认的名称来映射(如果是自定以的方法名,需要再ViewSet中显式的定义并实现,然后在下方的字典参数中注册)
# path("user_GenericViewSet/", views.UserGenericViewSet.as_view({
#     "get": "list",
#     "post": "create",
# })),
# re_path('^user_GenericViewSet/(?P<pk>\d+)$', views.UserGenericViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "delete": "destroy",
#     }
# )),
# # ReadOnlyViewSet(注意,以下的映射需要以默认的名称来映射(如果是自定以的方法名,需要再ViewSet中显式的定义并实现,然后在下方的字典参数中注册)
# path("user_ReadOnlyViewSet/", views.UserReadOnlyMixin.as_view({
#     "get": "list",
#     "post": "create",
# })),
# re_path('^user_ReadOnlyViewSet/(?P<pk>\d+)$', views.UserReadOnlyMixin.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "delete": "destroy",
#         # "delete":"delete"
#     }
# )),
# #     ModelViewSet
# path("user_ModelViewSet/", views.UserModelViewSet.as_view({
#     "get": "list",
#     "post": "create",
# })),
# re_path('^user_ModelViewSet/(?P<pk>\d+)$', views.UserModelViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "delete": "destroy",
#     }
# )),

# 简单路由
# router = SimpleRouter()
# 提供(生成)更多的路由
# DefaultRouter与SimpleRouter的区别是,DefaultRouter会多附带一个默认的API根视图，返回一个包含所有列表视图的超链接响应数据。
router = DefaultRouter()
""" """
# 注册路由(该操作会将基于ViewSet的视图集视图类生成对应的一系列路由)
# router.register("user_GenericViewSet", views.UserGenericViewSet, basename="user_GenericViewSet")
# router.register("user_ModelViewSet", views.UserModelViewSet, basename="ModelViewSetReg")
router.register("info", UserModelViewSet, basename="info")
router.register("register",UserRegisterModelViewSet,basename='register')
router.register("history", WSHModelViewSet, basename="history")
router.register("star", WordStarModelViewSet, basename="star")

# print(f"@router.urls={router.urls}")
urlpatterns += router.urls
# print(urlpatterns)
# """ 分行打印路由数组,并且计数"""
# cnt=0
# for url in urlpatterns:
#     cnt+=1
#     print(f"url:@cnt={cnt},@url={url}")

# router.register(r"user", views.UserApiViewSet)
# # 将DRF框架生成的连接插入到urlpatterns中
# urlpatterns += router.urls
# 通过启动项目,可以看到终端会打印出一系列的urlpatterns(routers.urls生成的)
# [
# <URLPattern '^user/$' [name='user-list']>,
# <URLPattern '^user/(?P<pk>[^/.]+)/$' [name='user-detail']>
# ]
# 譬如使用http://127.0.0.1:8000/user/user/来访问DRF提供的路由
