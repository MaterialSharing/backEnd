from django.urls import path, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import WordNotesModelViewSet

# app_name = 'word'
urlpatterns = [
    # re_path(r'index', views.index, name="index"),
    path('index_drf',views.IndexAPIView.as_view(),name="index_drf"),
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
    })),
    path('fuzzy/<str:spelling>/<int:start_with>/', views.WordMatcherViewSet.as_view({
        "get": "fuzzy_match"
    }),name = "fuzzy"),
    path('sum/<str:examtype>/', views.WordSumModelViewSet.as_view())
]
# router = SimpleRouter()
router=DefaultRouter()
# Api Root for current django app(word)
# The default basic root view for DefaultRouter
# http://127.0.0.1:8000/word/  访问改路由,您可以获得DRF提供的隶属于本模块的且被register注册过的若干模块的路由(url)
router.register("dict", views.WordModelViewSet, basename="dict_drf")
# router.register("word_matcher",views.WordMatcherViewSet)
router.register("cet4", views.Cet4WordsModelViewSet, basename="cet4")
router.register("cet6", views.Cet6WordsModelViewSet, basename="cet6")
router.register("neep", views.NeepWordsModelViewSet, basename="neep")
router.register("note", WordNotesModelViewSet, basename='note')

# http://127.0.0.1:8000/word/word_ViewSet/1000/
urlpatterns += router.urls
# print(f"@router.urls={router.urls}@word")
