import hashlib

from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from cxxulib.static_values import uob
from user.models import User
from user.serializer import UserModelSerializer

Res = Response


class Login(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def login(self, request):
        return Res("welcome!please login!")
        pass

    def dologin(self, request):
        # 注意request在drf中和原生django中的对象类型的区别
        # user = get_object_or_404(User, username=request.POST['account'])
        # user = get_object_or_404(User, name=request.data['account'])
        user = uob.filter(name=request.data['account']).first()
        # 改用户状态合法!,则允许其尝试登录
        print("@user:", user)
        # return Res("debgin!")
        if user.status == 0:
            md5 = hashlib.md5()
            # 获取用户输入的密码以及用户的干扰盐(得到salt_password)
            print("@password_salt:", user.password_salt)
            salt_password = user.password_salt + request.data['password']
            print("@salt_password:", salt_password)
            # 将利用md5对象的update方法对字符串加密
            md5.update(salt_password.encode('utf-8'))
            password_hash_wait = md5.hexdigest()
            # 判断用户输入的密码和加密后的密码是否一致
            if user.password_hash == password_hash_wait:
                print('登录成功')
                # 操作session实现登录状态的保持.
                # request.session['user_id'] = user.id
                ser = UserModelSerializer(user)
                data = ser.data
                # 以字典的形式添加到session字典(一个条目)
                # key = user.uid
                key = user.name
                key = str(key)
                key = 'cxxu'
                # 尝试将data作为value添加到session字典中
                request.session[key] = data
                index_url = reverse('info-list')
                ret = redirect(index_url)

                print(ret)
                # return Res(data)
                return Res({"login_status": "success"})
            else:
                print('登录失败')
                return Res({"login_status": "fail"})
        else:
            print('无效登录(account/password)')
            # return False
            return Res({"login_status": "failed"})

    def logout(self, request):
        # pass
        key = 'cxxu'
        del request.session[key]
        return Res("logout!")

    def fetch_user(self, req):
        sess = req.session
        print("session=", sess)
        # print("session.keys=", sess.keys())
        print("session.cxxu=", sess.get('cxxu'))
        # return Response({"msg": "fetch_user"})
        return Res(sess.get('cxxu'))