from deprecated.classic import deprecated
from django.urls import path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import study, study_separate

# from .views import Review
# 启用命名空间
# 关于导包错误:idea并不会察觉一个包中是否缺少__init__.py文件!
# No module named 'scoreImprover.views.study'; 'scoreImprover.views' is not a package
from .views.study import StudyModelViewSet

app_name = 'improver'
urlpatterns = [
    # path('',  study_separate.index, name='index'),
    # path('review/<int:size>', Review.as_view(), name='sized_review'),

    # path('review', Review.as_view(), name='review'),
    # re_path(),

    # path('last_see',study_separate.NeepStudyModelViewSet.as_view(){
    #     "put":
    # })
    # 注册路由的时候纪要注意url拼写,也要注意是否是对应的视图类(视图函数)/ModelViewSet(特别是由多个类似名字的序列化器)
    # apifox的测试连接中,对于put/post,需要注意结尾的斜杠,应该要加上,或者总是加上
    # 如果找不到页面,可以看后台终端的输出,对于失败的请求会给出详细错误
    # path('neep/create_unique', study_separate.NeepStudyModelViewSet.as_view({
    #     "put": "create_unique"
    # })),
    # re_path('^neep/recently/(?P<days>(\-|\+)?\d+(\.\d+)?)$', study_separate.NeepStudyModelViewSet.as_view({
    #     "get": "recently"
    # })),
    # re_path('^neep/timedelta/(?P<unit>\w+)/(?P<value>(\-|\+)?\d+(\.\d+)?)$', study_separate.NeepStudyModelViewSet.as_view({
    #     "get": "recently_unitable"
    # })),
    # path('neep/refresh/', study_separate.NeepStudyModelViewSet.as_view({
    #     "put": "refresh"
    # })),
    # path('<str:examtype>/', study_separate.NeepStudyModelViewSet.as_view(), name='neep_study'),
    path('study/refresh/', StudyModelViewSet.as_view({
        'put': "refresh"
    })),
    re_path('^study/familiarity/(?P<change>add|sub)/$', StudyModelViewSet.as_view({
        "put": "familiarity_change1"
    }), name="familiarity_change1"),
    # 注意,下方的路由pattern中,如果使用转换器(str:examtype)会匹配到本意的4/6/8,因此,需要解决冲突,使用更加今昔的匹配规则,防止某些不恰当的匹配造成多余的困扰
    # path('study/<str:examtype>/',
    re_path('^study/(?P<examtype>cet[46]|neep)/$', study_separate.RefresherModelViewSet.as_view({
        "put": "refresh"
    }), name="refresh"),
    re_path('study/(?P<examtype>cet[46]|neep)/familiarity/<str:change>/', study_separate.RefresherModelViewSet.as_view({
        "put": "familiarity_change1"
    }), name="familiarity_change1"),
    #复习
    # 从考纲词库中抽查一组单词
    path('review/<str:examtype>/<int:size>/', study_separate.RandomInspectionModelViewSet.as_view(
        {
            "get": "get_words_random"
        }
    ), name='sized_review'),
]

router = DefaultRouter()

# router.register("review",)
# 基于视图集自动生成常用路由
# router.register("study/filter", study.StudyModelViewSet, basename="study")
router.register("study", study.StudyModelViewSet, basename="study")


@deprecated("use more generic router resolutoin above instead")
def neep_urls(self):
    router.register("neep_detail", study_separate.NeepStudyDetailViewSet)
    router.register("neep/detail", study_separate.NeepStudyDetailViewSet)
    router.register("study/neep/detail", study_separate.NeepStudyDetailViewSet)
    # 查看学习记录


# neep_urls()
router.register("neep", study_separate.NeepStudyModelViewSet, basename="neep")
router.register("cet4", study_separate.Cet4StudyModelViewSet, basename="cet4")
router.register("cet6", study_separate.Cet6StudyModelViewSet, basename="cet6")

# 将生成的路由显示的添加到urlpatterns
urlpatterns += router.urls
