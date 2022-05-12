from rest_framework.serializers import ModelSerializer

from word.models import Word, WordNotes, Cet4WordsReq, Cet6WordsReq, NeepWordsReq


class WordModelSerializer(ModelSerializer):
    class Meta:
        model = Word
        # fields=["spelling"]
        fields = "__all__"


class WordNotesModelSerializer(ModelSerializer):
    class Meta:
        model = WordNotes
        fields = "__all__"
# 考纲表不需要提供接口全部接口
class Cet4WordsReqModelSerializer(ModelSerializer):
    class Meta:
        model=Cet4WordsReq
        fields="__all__"
class Cet6WordsReqModelSerializer(ModelSerializer):
    class Meta:
        model=Cet6WordsReq
        fields="__all__"
class NeepWordsReqModelSerializer(ModelSerializer):
    class Meta:
        model=NeepWordsReq
        fields="__all__"