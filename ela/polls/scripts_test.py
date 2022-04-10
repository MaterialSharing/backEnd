
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from django.test.utils import setup_test_environment
from django.test import Client
# from .models import Question


setup_test_environment()
client = Client()

 # get a response from '/'
response = client.get('/')
 # we should expect a 404 from that address; if you instead see an
 # "Invalid HTTP_HOST header" error and a 400 response, you probably
 # omitted the setup_test_environment() call described earlier.
response.status_code
 # on the other hand we should expect to find something at '/polls/'
 # we'll use 'reverse()' rather than a hardcoded URL
response = client.get(reverse('polls:index'))
reverse('polls:detail',args=[1] )#'/polls/1/'
response=client.get(reverse('polls:detail',args=[1]))
response.status_code
response.content
response.context['latest_question_list']