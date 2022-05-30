"""backEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAuthenticated

# schema_view = get_schema_view(title='backEnd API')
schema_view = get_schema_view(
    openapi.Info(
        title="backEnd API",
        default_version='v1',
        description="backEnd API",
    ),
    public=True,
    # permission_classes=(IsAuthenticated,),
)

urlpatterns = [
    # 检测路由冲突:当某些个路由可能潜在的发生冲突,可以在这里注释掉其他路由来排查问题
    # 此处的path函数的第一个参数的含义是应用名,第二个参数(include()指出应用下的子路由配置对象),来匹配并路由后续的任务

    # 注意slash(`/`不要漏掉)
    path('admin/', admin.site.urls),
    # 可选的'swagger'参数,可以指定为其他名称
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', include_docs_urls('DRF_docs_coreApi')),
    path('polls/', include('polls.urls')),
    path('word/', include('word.urls')),
    path('improver/', include('scoreImprover.urls')),
    path('main/', include('main.urls')),
    path('api/', include("user.urls")),
    path('user/', include('user.urls')),
    # path('blog/',include('blog.urls')),
    #     采用DRF风格的路由
    # path('api/', include("user_raw.urls")),
]
