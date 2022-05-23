from scoreImprover.models import NeepStudy

neep_study_ob=NeepStudy.objects
s1=neep_study_ob.create(user_id=1,wid_id=1)
print(s1)
