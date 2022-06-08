from django.db.models import CharField
from django.db.models.functions import Length

from scoreImprover.models import NeepStudy
from scoreImprover.views import neep_study_ob
# neep_study_ob.annotate()
from word.models import NeepWordsReq, WordMatcher
from word.views import wob, wmob

wmob = WordMatcher.objects


# 使用数据函数查询字符串长度,执行相关判断
# neep_req_ob = NeepWordsReq.objects
# # CharField.register_lookup(Length)
# queryset = neep_req_ob.filter(spelling__length__gt=16)
# queryset = neep_req_ob.filter(spelling__length)

class UpdateWordMatcher:
    # 填充单词模糊匹配数据库支持(模糊推荐算法)
    # 测试两个例子
    def update(self):
        # sub_dict_set = wob.all()
        sub_dict_set = wob.all()[:2]
        for item in sub_dict_set:
            # print(item)
            char_set = set(item.spelling)
            chars = list(char_set)
            chars.sort()
            chars_str = "".join(chars)
            # return chars_str
            print(chars_str)
            d = {"spelling": item.spelling, "char_set": chars_str}
            wmob.create(,
            # chars=list(char_set).sort()
            # print(chars)
#
# spelling = "acqueintane"
# spelling_len = len(spelling)
# left_len = spelling_len * 0.75
# right_len = spelling_len * 1.25
# chars=list(set(spelling))
# chars.sort()
# spelling_chars = "".join(chars)
# queryset = wmob.filter(spelling__length__gte=left_len) & wmob.filter(
#     spelling__length__lte=right_len) & wmob.filter(char_set__contains=spelling_chars)
# queryset = queryset.filter(spelling__startswith=spelling[:2])
#
# queryset
#
# data = {
#     # "id": 1,
#     "last_see_datetime": "2022-05-13T10:26:40.857357Z",
#     "familiarity": 1,
#     "wid": 1,
#     "uid": 1
# }
# item = NeepStudy(**data)
# wid = 1
# uid = 1
# queryset = neep_study_ob.filter(wid=wid) & neep_study_ob.filter(uid=uid)
# instance = queryset[0]
