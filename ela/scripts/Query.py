#遇到类似: django.db.utils.OperationalError: (2006, 'Server has gone away')的错误时
# 关闭掉当前的交互终端,然后重新启动一个终端
import django.db
django.db.close_old_connections()

from django.utils import timezone
from word.models import Word
# User.objects.create(name="testScriptUser")
# test DRF api
from user.serializer import UserSerializer
from user.models import User
uob=User.objects
user=uob.get(pk=7)


wob=Word.objects
word=Word.objects.all()[:2]
print(word)


user_s=UserSerializer(user)
type(user_s)
# 以字典的形式查看所有字段
user_s.data
# 一次性查看多个数据
users=uob.all()
## 需要显示的说明由多个记录被用来构造这个序列化器对象
users_serializer=UserSerializer(users,many=True)
users_serializer.data

# 反序列化(数据输入)
data={"name":"cxxu_testSer","signin":5}
user_s=UserSerializer(data=data)
user_s.is_valid()
user_s.data
# 如果False
user_s.errors
# 尝试修改(写数据库)
user_s=UserSerializer(user, data, partial=True)
user_s.is_valid()
user_s.save()
# 查看修改结果
uob.get(name="cxxu_testSer")

data={"name":"cxxu_new","signupdate":timezone.now().date()}
user_s=UserSerializer(data=data)
user_s.is_valid()
user_s.save()


