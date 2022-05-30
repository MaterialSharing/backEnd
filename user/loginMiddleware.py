# 中间件的编写方式有两种:
# https://docs.djangoproject.com/en/4.0/topics/http/middleware/

# class SimpleMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         response = self.get_response(request)
#
#         # Code to be executed for each request/response after
#         # the view is called.
#
#         return response
import re

from django.shortcuts import redirect


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("LoginMiddleware init")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        # 执行一些检查和判断
        accessible_urls = ["/user/login/", "/user/register/",'user/logout/','/user/dologin/']
        if re.match(r'/user/', path):
            if path not in accessible_urls:
                # return redirect("/user/login/")
                # 对访问的url进行状态检查
                # 如果没有登录,则跳转到登录页面
                # request.session.get()返回结果两种:
                # 1.如果session中没有该key,则返回None(对这种情况进行进一步登录要求处理
                # 2.如果session中有该key,则返回该key对应的value
                # 找不到合法session,则跳转到登录页面(使用not反转进入分支处理)
                if not request.session.get("cxxu"):
                    return redirect("/user/login/")
        # response = self.get_response(request)
        # return response
        #     return redirect('/user/info/login')

        # 放行(不需要登录/信息验证成功)
        response = self.get_response(request)
        return response
