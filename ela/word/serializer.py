from rest_framework.serializers import ModelSerializer

from word.models import Word


class WordModleSerializer(ModelSerializer):
    class Meta:
        model = Word
        # fields=["spelling"]
        fields = "__all__"
