
from django.urls import URLPattern, path,re_path
from . import views
# 注意大小写要区分,不要过分依赖于补全!
urlpatterns=[
    # path('',views.index,name='index'),
    # as_view()注意小写V
    path('',views.UserApiView.as_view(),name='userPost'),
    # path(r'^(?P<pk>)$',views.UserApiView.as_view(),name='userCheck'),
    # path(r'^user/$',views.UserApiView.as_view(),name='userCheck'),

    path('userAdd/<str:name>',views.userAdd,name='userAdd'),
    path('userCheck/<str:name>',views.userCheck,name='userCheck')
]