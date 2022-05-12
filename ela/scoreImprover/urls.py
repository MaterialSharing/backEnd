from django.urls import path, re_path
from rest_framework.routers import SimpleRouter

from . import views
from .views import Review

urlpatterns = [
    path('', views.index, name='index'),
    path('review/<int:size>', Review.as_view(), name='sized_review'),
    # path('review', Review.as_view(), name='review'),
    # re_path(),
]

router = SimpleRouter()
# router.register("review",)
