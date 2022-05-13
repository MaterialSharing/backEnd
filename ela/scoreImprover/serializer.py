from rest_framework.serializers import ModelSerializer

from scoreImprover.models import NeepStudy, LongSentences, Cet4Study, Cet6Study


class LongSentencesModelSerializer(ModelSerializer):
    class Meta:
        model = LongSentences
        fields = "__all__"


class NeepStudyModelSerializer(ModelSerializer):
    class Meta:
        model = NeepStudy
        fields = "__all__"
        # fields+=""
        # 默认关联深度
        # 关联外键(表)的深度为1
        # depth=1

class Cet4StudyModelSerializer(ModelSerializer):
    class Meta:
        model = Cet4Study
        fields = "__all__"


class Cet6StudyModelSerializer(ModelSerializer):
    class Meta:
        model = Cet6Study
        fields = "__all__"
