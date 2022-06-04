from rest_framework.response import Response

from scoreImprover.models import Cet4Study, Cet6Study, NeepStudy, Study
from user.models import User, WordSearchHistory, WordStar
from word.models import Cet4WordsReq, Cet6WordsReq, NeepWordsReq

Res=Response
uob = User.objects
wob = User.objects
c4ob = Cet4WordsReq.objects  # type: Cet4WordsReq
c6ob = Cet6WordsReq.objects  # type: Cet6WordsReq
neepob = NeepWordsReq.objects  # type: NeepWordsReq
wshob = WordSearchHistory.objects  # type: WordSearchHistory
wsob = WordStar.objects  # type: WordStar
cet4_study_ob = Cet4Study.objects
cet6_study_ob = Cet6Study.objects
neep_study_ob = NeepStudy.objects
study_ob = Study.objects

