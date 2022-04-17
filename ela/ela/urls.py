"""ela URL Configuration

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
from django.urls import path,include
# route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。
urlpatterns = [
    path('',include('index.urls')),
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
    path('word/',include('word.urls')),
    path('scoreImprover/',include('scoreImprover.urls')),
    path('main/',include('main.urls')),
    # 注意slash(`/`不要漏掉)
    path('user/',include('user.urls'))
    # path('blog/',include('blog.urls')),
]
