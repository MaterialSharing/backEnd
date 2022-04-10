from django.urls import path

from . import views
# 一下路由都是基于路径polls下(是polls的子页)
""" 
The question_id=34 part comes from <int:question_id>. Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function. The question_id part of the string defines the name that will be used to identify the matched pattern, and the int part is a converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.
 """
app_name='polls'
# URLconf for Generic Views version.
urlpatterns = [
    # The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # detail:question detial (with choices)
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('qG/',views.QueryListView.as_view(),name="queryG"),
    path('q/',views.query,name="query"),
    path('addQuestion/<str:question>/',views.addQuestion,name='addQuestion'),


]
""" the old version of views router """
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('addQuestion/<str:question>/',views.addQuestion,name='addQuestion'),
#     path('q/',views.query,name="query"),
# ]