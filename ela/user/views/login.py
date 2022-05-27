import hashlib

from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializer import UserModelSerializer

Res = Response


class Login(ModelViewSet):
    def login(self, request):
        pass

    def dologin(self, request):
        # 注意request在drf中和原生django中的对象类型的区别
        user = get_object_or_404(User, username=request.POST['username'])
        if user.status == 0:
            md5 = hashlib.md5()
            # 获取用户输入的密码以及用户的干扰盐(得到salt_password)
            salt_password = request.POST[' password'] + user.password_salt
            # 将利用md5对象的update方法对字符串加密
            md5.update(salt_password.encode('utf-8'))
            password_hash_wait = md5.hexdigest()
            # 判断用户输入的密码和加密后的密码是否一致
            if user.password_hash == password_hash_wait:
                print('登录成功')
                # 操作session实现登录状态的保持.
                # request.session['user_id'] = user.id
                ser=UserModelSerializer(user)
                data=ser.data
                # 以字典的形式添加到session字典(一个条目)
                request.session['user_id']=data['id']
                return Res({"login_status": "success"})
        else:
            print('无效登录(account/password)')
            # return False
            return Res({"login_status": "failed"})

    def logout(self, request):
        pass
