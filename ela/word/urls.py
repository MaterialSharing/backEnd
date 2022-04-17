from django.urls import path,re_path
from . import views
urlpatterns=[
    re_path(r'index',views.index,name="index"),
    path(r'<slug:word>/',views.WordAPIView.as_view(),name='wordQuery'),
    re_path(r'(?P<word>^\w*$)/',views.WordAPIView.as_view(),name='wordQuery'),
    path(r'word/',views.WordAPIView.as_view(),name='word')
]
