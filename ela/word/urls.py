from django.urls import path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import WordNotesModelViewSet

# app_name = 'word'
urlpatterns = [
    # re_path(r'index', views.index, name="index"),
    path('index_drf', views.IndexAPIView.as_view(), name="index_drf"),
    # path(r'<slug:word>/',views.WordAPIView.as_view(),name='wordQuery'),
    # re_path(r'^(?P<word>\w*)/$',views.WordAPIView.as_view(),name='wordQuery'),
    # path(r'word/',views.WordAPIView.as_view(),name='word'),

    # <str:spelling>将被转换为正则: ?P<spelling>[^/]+)/\\Z
    path('dict/<str:spelling>/', views.WordModelViewSet.as_view({
        "get": "dict"
    }), name='dict_spelling'),

    path('fuzzy/', views.WordMatcherViewSet.as_view({"get": "list"})),
    path('fuzzy/<str:spelling>/', views.WordMatcherViewSet.as_view({
        "get": "fuzzy_match_simple"
    }), name='fuzzy_match_simple'),
    path('fuzzy/<str:spelling>/<int:start_with>/', views.WordMatcherViewSet.as_view({
        "get": "fuzzy_match"
    }), name="fuzzy"),
    path('sum/<str:examtype>/', views.WordSumModelViewSet.as_view(), name="sum"),
    path('test/', views.WordDemoTestAPIView.as_view(), name='test'),

]
# router = SimpleRouter()
router = DefaultRouter()
# Api Root for current django app(word)
# The default basic root view for DefaultRouter
# http://127.0.0.1:8000/word/  访问改路由,您可以获得DRF提供的隶属于本模块的且被register注册过的若干模块的路由(url)
# 关于drf的reverse()解析,注意下方的basename参数
#basename参数仅仅指定了路由的前缀,而不完整的路由别名(因为,register一次性会产生5条路由,每个路由的别名都是基于basename参数的)
#根据CRUD操作,完整的路由应该是basename-list,basename-create,basename-retrieve,basename-update,basename-destroy
# 注意,这里的basename和score improver模块中的路由有点类似,容易重复(可以考虑启用命命名空间)
router.register("dict", views.WordModelViewSet, basename="dict")
# router.register("word_matcher",views.WordMatcherViewSet)
router.register("cet4", views.Cet4WordsModelViewSet, basename="cet4")
router.register("cet6", views.Cet6WordsModelViewSet, basename="cet6")
router.register("neep", views.NeepWordsModelViewSet, basename="neep")
router.register("note", WordNotesModelViewSet, basename='note')

# http://127.0.0.1:8000/word/word_ViewSet/1000/
urlpatterns += router.urls
# print(f"@router.urls={router.urls}@word")
