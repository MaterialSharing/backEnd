from scoreImprover.serializer import NeepStudyModelSerializer

ser=NeepStudyModelSerializer()
print(repr(ser))
# NeepStudyModelSerializer():
#     id = IntegerField(read_only=True)
#     last_see_datetime = DateTimeField(read_only=True)
#     familiarity = IntegerField(help_text='熟练度', max_value=2147483647, min_value=-2147483648, required=False)
#     user = PrimaryKeyRelatedField(queryset=User.objects.all())
#     wid = PrimaryKeyRelatedField(queryset=NeepWordsReq.objects.all())