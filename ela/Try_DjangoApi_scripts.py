# Import the model classes we just wrote.
from polls.models import Choice, Question  
Question.objects.all()

from django.utils import timezone
q=Question(question_text="what is new content?",pub_date=timezone.now())
q.save()
# auto fileds:id
# q.id
print(q.question_text)
print(q.pub_date)
q.question_text="what's update?"
q.save()
Question.objects.all()

Question.objects.get(pk=1)
q=Question.objects.get(pk=1)


Question.objects.filter(id=1)
Question.objects.filter(question_text__startswitch='what')

from polls.models import ela