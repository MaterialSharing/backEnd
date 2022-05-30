from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from scoreImprover.models import NeepStudy, LongSentences, Cet4Study, Cet6Study
from word.serializer import Cet4WordsReqModelSerializer


class LongSentencesModelSerializer(ModelSerializer):
    class Meta:
        model = LongSentences
        fields = "__all__"


class NeepStudyModelSerializer(ModelSerializer):
    # 使用read_only=True，可以让前端不需要传入这些仅仅用户显示的字段
    spelling = serializers.CharField(source="wid.spelling", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = NeepStudy
        # fields = "__all__"
        # 关于配置(列表中的各个项)行中的逗号:由于copilot AI 会内敛提示补齐,导致我误以为是有逗号的,而实际上要按下tab,才会实际产生逗号!
        fields = [
            'id',
            'last_see_datetime',
            'familiarity',
            'user',
            'user_name',
            'wid',
            'spelling',
        ]
        # fields+=""
        # 默认关联深度
        """关联深度(depth作为总开关),如果有多个外键,depth将统一设置深度为1
        默认的深度为0"""
        # 关于depth的文档:https://www.django-rest-framework.org/api-guide/serializers/#specifying-nested-serialization
        # 关联外键(表)的深度为1(仅显示外键字段(一对多)字段对象的主机(id/pk))
        # depth = 0(default)
        # depth = 1
        # 如果设置为1,那么在序列话的时候,必须传入的是外键对象,否则报错(仅传入外键对象的id序列化器不认帐)
        # 所以我们保持默认(depth=0)
        # 如果有特殊需求,可以针对个别属性进行depth提升,或者再创建一个只读的提供深层信息的detailModelSerializer类,然后在这个类中进行depth提升


class Cet4StudyModelSerializer(ModelSerializer):
    # spelling=serializers.CharField(source='cet4wordsreq.spelling',read_only=True)
    # spelling=serializers.CharField("test catch spelling.")
    #     "id": 6,
    #             "last_see_datetime": "2022-05-15T14:16:51.015432Z",
    #             "familiarity": 2,
    #             "user": 2,
    #             "wid": 4
    class Meta:
        model = Cet4Study
        # fields = "__all__"
        # 这里采用的模型的属性方法(不需要做read_only设置)
        fields = [
            'id',
            'last_see_datetime',
            'familiarity',
            'user',
            'user_name',
            'wid',
            'spelling',
            # 'wid_obj'
        ]
        read_only_fields = [
            'spelling',
            'user_name'
        ]


class Cet6StudyModelSerializer(ModelSerializer):
    # spelling = serializers.CharField(source="wid.spelling")
    # user_name = serializers.CharField(source="user.name")

    class Meta:
        model = Cet6Study
        # fields = "__all__"
        fields = [
            'id',
            'last_see_datetime',
            'familiarity',
            'user',
            'user_name',
            'wid',
            'spelling',
            'user_name'
        ]
        # read_only_fields似乎对外键无效
        # read_only_fields = [
        #     'spelling',
        #     'user_name'
        # ]


# 我们可以为同一个模型指定多个适用于不同场景的序列化器
# (譬如设置有外键的模型的序列化,可以设置具有不同关联层次(显示效果)的序列化器
class NeepStudyDetailModelSerializer(ModelSerializer):
    """显示深层关联信息"""
    # spelling=serializers.CharField(default="try spelling field extra")
    # 你可以先不适用read_only=True选项(当然,不去显示设置的换,是Fasle)
    # 这样就可以通过serialIzer.FiledName()能够检测这个source的取值是否是一个有效的模型字段
    # 采用source的方案的话,source的值是一个基于Meta.model的对象调用属性的语句
    spelling = serializers.CharField(source="wid.spelling", read_only=True)
    user_name = serializers.CharField(source="user.name", read_only=True)

    class Meta:
        model = NeepStudy
        # fields = "__all__"
        fields = [
            'id',
            'last_see_datetime',
            'familiarity',
            'user',
            'wid',
            'spelling',
            'user_name'
        ]

        # fields+=""
        # 默认关联深度
        # 关联外键(表)的深度为1
        # depth = 1
        # depth=0(默认值)
