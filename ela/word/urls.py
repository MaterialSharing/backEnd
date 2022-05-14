from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views
from .views import WordNotesModelViewSet

urlpatterns = [
    re_path(r'index', views.index, name="index"),
    # path(r'<slug:word>/',views.WordAPIView.as_view(),name='wordQuery'),
    # re_path(r'^(?P<word>\w*)/$',views.WordAPIView.as_view(),name='wordQuery'),
    # path(r'word/',views.WordAPIView.as_view(),name='word'),
]
router = SimpleRouter()
router.register("dict", views.WordModelViewSet, basename="word")
router.register("cet4", views.Cet4WordsModelViewSet, basename="cet4")
router.register("cet6", views.Cet6WordsModelViewSet, basename="cet6")
router.register("neep", views.NeepWordsModelViewSet, basename="neep")
router.register("note", WordNotesModelViewSet, basename='note')

# http://127.0.0.1:8000/word/word_ViewSet/1000/
urlpatterns += router.urls
# print(f"@router.urls={router.urls}@word")
