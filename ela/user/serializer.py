from rest_framework import serializers

from user.models import User

uob=User.objects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    def validate_name(self,value):
        if "cxxu" not in value.lower():
            raise serializers.ValidationError("the user is created by cxxu")
        return value
    def validate(self,data):
        return data
    def update(self,instance,validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.signin=validated_data.get("signin",instance.signin)
        instance.save()
        return instance
    def save(self,validated_data):
        return uob.create(**validated_data)