# Import the model classes we just wrote.
from polls.models import Choice, Question
from django.utils import timezone

# 如果模型字段和数据库字段不匹配,可能导致拆线呢失败
Question.objects.all()
q = Question(question_text="what is new content?", pub_date=timezone.now())
q.save()
qob = Question.objects
qob.all()
# auto fileds:id
# q.id

print(q.question_text)
print(q.pub_date)
q.question_text = "what's update?"
q.save()
Question.objects.all()

Question.objects.get(pk=1)
q = Question.objects.get(pk=1)

Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='what')

# creat choice object(by question object)
c = q.choice_set.create(,
c.question

# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
q.choice_set.count()
current_year = timezone.now().year
Choice.objects.filter(question__pub_date__year=current_year)
