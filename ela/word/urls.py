from django.urls import path,re_path
from rest_framework.routers import SimpleRouter

from . import views
urlpatterns=[
    re_path(r'index',views.index,name="index"),
    # path(r'<slug:word>/',views.WordAPIView.as_view(),name='wordQuery'),
    # re_path(r'^(?P<word>\w*)/$',views.WordAPIView.as_view(),name='wordQuery'),
    # path(r'word/',views.WordAPIView.as_view(),name='word'),
]
router=SimpleRouter()
router.register("word_ViewSet",views.WordModelViewSet,basename="word")
# http://127.0.0.1:8000/word/word_ViewSet/1000/
urlpatterns+=router.urls
print(f"@router.urls={router.urls}@word")
