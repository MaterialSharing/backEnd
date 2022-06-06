# from cxxulib.printer import print1
# from word.serializer import Cet4WordsReqModelSerializer
# from word.views import c4ob
#
# queryset = c4ob.all()
# serializer_class = Cet4WordsReqModelSerializer
# ser = serializer_class
# size = queryset.count()
# print("@@size:", size)
# words_objs = []
#
# for pk in random_words_pks:
#     print(pk)
#     word = c4ob.get(pk=pk)
#     words_objs.append(word)
#     ser = serializer_class(instance=word)
#
#     print(ser.data)
#
# # print1(words_objs)
# # ser=serializer_class(instance=words_objs,many=True)
#
# q_app = c4ob.filter(spelling__startswith='app')
# q_in=c4ob.filter(wordorder__in=random_words_pks)
#
# q_app
# # type(q_app)
#
# # c4ob.all()[:20]
# words=serializer_class(instance=q_app,many=True)
# # print(words.data)
