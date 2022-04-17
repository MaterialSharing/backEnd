from user.models import User
from word.models import Word
# User.objects.create(name="testScriptUser")

wob=Word.objects
word=Word.objects.all()[:2]
print(word)

