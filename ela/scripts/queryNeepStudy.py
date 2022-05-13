from scoreImprover.models import NeepStudy

data = {
    # "id": 1,
    # "last_see_datetime": "2022-05-13T10:26:40.857357Z",
    "familiarity": 1,
    "uid":1,
    "wid": 1
}
item = NeepStudy(**data)
print(item)