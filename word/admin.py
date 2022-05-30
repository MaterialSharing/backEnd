from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Cet4WordsReq,Cet6WordsReq,NeepWordsReq,Word])