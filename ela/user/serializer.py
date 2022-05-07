from rest_framework import serializers

from user.models import User

uob = User.objects


# 外部验证函数(可以用户多个模型共享,但是不多见);定义完成后,需要改通过参数的形式添加到指定的序列化类中字段的构造器(validators=[chekcerxxx]参数)
def name_common_checker(value):
    if "cxxu" not in value.lower():
        raise serializers.ValidationError("the user is created by cxxu")
    return value


# 只用最基本的Serializer类来实现serializer(不使用ModelSerializer中的功能)
# 该序列化器的名称后缀以基本的Serializer结尾
class UserSerializer(serializers.Serializer):
    # 定义元数据类
    class Meta:
        # 指定序列化器是使用的模型类
        model = User
        # 指明使用的字段是给模型的全部字段.
        # fields = "__all__"
        #     可以通过数组,指定个别字段
        fields = ["name", "signin", "signupdate", ]

    # 基本的校验方式:通过指定字段的参数来传递限制条件
    name = serializers.CharField(max_length=30)
    signin = serializers.IntegerField(max_value=10000, min_value=0, error_messages={
        "min_value": "the sign in days must be:age>=0",
        "max_value": "the Age filed must be:age<=10000 "
    })

    # 序列化器检查数据是否合规
    '''serializer 是直接和数据请求/提交打交道,将数据规范性检查也一并安排在模型的序列化器中是实现'''

    # 针对某些字段实现更加复杂的验证规则
    # 需要以validate_filedName的格式来定义变量名,否则is_validate()无法知道这个检测规则以及该规则适用于哪个字段的检测
    def validate_name(self, value):
        # if "cxxu" not in value.lower():
        #     raise serializers.ValidationError("the user is created by cxxu")
        if value in ["null", "python", "django"]:
            raise serializers.ValidationError(detail="the student name must not be python/django/null",
                                              code="validate_name")
        return value

    # 为序列号器实现update方法,使得序列化器能够帮助我们完成数据更新
    def update(self, instance, validated_data):
        # instance.name = validated_data.get("name", instance.name)
        # instance.signin = validated_data.get("signin", instance.signin)
        # 通过遍历来设置
        for key, value in validated_data.items():
            #     Sets the named attribute on the given object to the specified value.
            # setattr(x, 'y', v) is equivalent to ``x.y = v''
            setattr(instance, key, value)
        instance.save()
        return instance

    # 向数据库添加数据
    def create(self, validated_data):
        """
        方法名固定为create,且参数也是固定名为validate_date
        :param validated_data: 该参数就是验证成功后的结果
        :return: 返回模型对象User实例
        """
        user = uob.create(**validated_data)
        return user


# 继承于ModelSerializer来编写比较简化的代码
# 该序列化器的名称以ModelSerializer结尾
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
