#遇到类似: django.db.utils.OperationalError: (2006, 'Server has gone away')的错误时
# 关闭掉当前的交互终端,然后重新启动一个终端

from word.models import Word
# User.objects.create(name="testScriptUser")


wob=Word.objects
word=Word.objects.all()[:2]
print(word)

# test DRF api
from user.serializer import UserSerializer

from user.models import User
uob=User.objects
user=uob.get(pk=7)
user_serializer=UserSerializer(user)
type(user_serializer)
user_serializer.data
