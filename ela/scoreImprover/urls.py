from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views
from .views import Review

urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:size>', Review.as_view(), name='sized_review'),
    # path('review', Review.as_view(), name='review'),
    # re_path(),

    # path('last_see',views.NeepStudyModelViewSet.as_view(){
    #     "put":
    # })
    # 注册路由的时候纪要注意url拼写,也要注意是否是对应的视图类(视图函数)/ModelViewSet(特别是由多个类似名字的序列化器)
    # apifox的测试连接中,对于put/post,需要注意结尾的斜杠,应该要加上,或者总是加上
    # 如果找不到页面,可以看后台终端的输出,对于失败的请求会给出详细错误
    path('neep/create_unique', views.NeepStudyModelViewSet.as_view({
        "put": "create_unique"
    })),
    re_path('^neep/recently/(?P<days>(\-|\+)?\d+(\.\d+)?)$', views.NeepStudyModelViewSet.as_view({
        "get": "recently"
    })),
    re_path('^neep/timedelta/(?P<unit>\w+)/(?P<value>(\-|\+)?\d+(\.\d+)?)$', views.NeepStudyModelViewSet.as_view({
        "get": "recently_unitable"
    })),
    # path('neep/refresh/', views.NeepStudyModelViewSet.as_view({
    #     "put": "refresh"
    # })),
    path('<str:examtype>/refresh/', views.RefresherModelViewSet.as_view({
        "put": "refresh"
    }))
]

router = SimpleRouter()

# router.register("review",)
# 基于视图集自动生成常用路由
router.register("neep", views.NeepStudyModelViewSet, basename="neep")
router.register("neep_detail", views.NeepStudyDetailViewSet)
router.register("neep/detail", views.NeepStudyDetailViewSet)
# 查看学习记录
router.register("cet4", views.Cet4StudyModelViewSet)
router.register("cet6", views.Cet6StudyModelViewSet)

# 将生成的路由显示的添加到urlpatterns
urlpatterns += router.urls
