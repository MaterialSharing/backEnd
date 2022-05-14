from scoreImprover.models import NeepStudy
from scoreImprover.views import neep_study_ob

data = {
    # "id": 1,
    "last_see_datetime": "2022-05-13T10:26:40.857357Z",
    "familiarity": 1,
    "wid": 1,
    "uid": 1
}
item = NeepStudy(**data)
wid = 1
uid = 1
queryset = neep_study_ob.filter(wid=wid) & neep_study_ob.filter(uid=uid)
instance = queryset[0]
