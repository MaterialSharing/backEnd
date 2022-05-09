from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from word.models import WordNotes, Cet4WordsReq, Cet6WordsReq, NeepWordsReq
from word.serializer import NeepWordsReqModelSerializer, WordNotesModelSerializer, Cet4WordsReqModelSerializer, \
    Cet6WordsReqModelSerializer



def index(request):
    return HttpResponse("scoreImprover!")


