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


class Cet4StudyModelSerializer(ModelSerializer):
    class Meta:
        model = Cet4Study
        fields = "__all__"


class Cet6StudyModelSerializer(ModelSerializer):
    class Meta:
        model = Cet6Study
        fields = "__all__"
