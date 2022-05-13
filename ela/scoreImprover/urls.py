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
]

router = SimpleRouter()

# router.register("review",)
# 基于视图集自动生成常用路由
router.register("neep", views.NeepStudyModelViewSet, basename="neep")
# 将生成的路由显示的添加到urlpatterns
urlpatterns += router.urls
