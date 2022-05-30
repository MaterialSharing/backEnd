from django.test import TestCase
from word.serializer import Cet4WordsReqModelSerializer, Cet6WordsReqModelSerializer, NeepWordsReqModelSerializer

from cxxulib.querysetDispatcher import QuerysetDispatcher
from query_scripts.inspectSerializer import ser
from scoreImprover.serializer import Cet4StudyModelSerializer, Cet6StudyModelSerializer, NeepStudyModelSerializer


class DispatcherTestCase(TestCase):
    def test_get_serializer_study(self):
        ser4 = QuerysetDispatcher.get_serializer_class_study("cet4")
        self.assertEqual(ser4, Cet4StudyModelSerializer)
        ser6 = QuerysetDispatcher.get_serializer_class_study("cet6")
        self.assertEqual(ser6, Cet6StudyModelSerializer)
        ser8 = QuerysetDispatcher.get_serializer_class_study("neep")
        self.assertEqual(ser8, NeepStudyModelSerializer)
        # print("@ser4,ser6,ser8:", ser4, ser6, ser8)

    def test_get_serializer_req(self):
        ser4 = QuerysetDispatcher.get_serializer_class_req("cet4")
        self.assertEqual(ser4, Cet4WordsReqModelSerializer)
        ser6 = QuerysetDispatcher.get_serializer_class_req("cet6")
        self.assertEqual(ser6, Cet6WordsReqModelSerializer)
        ser8 = QuerysetDispatcher.get_serializer_class_req("neep")
        self.assertEqual(ser8, NeepWordsReqModelSerializer)
        # print("@ser4,ser6,ser8:", ser4, ser6, ser8)

    def test_get_queryset_req(self):
        qs4 = QuerysetDispatcher.get_queryset_req("cet4")
        self.assertEqual(qs4.model, Cet4WordsReqModelSerializer.Meta.model)
        print("@qs4:", qs4, Cet4WordsReqModelSerializer.Meta.model)
        qs6 = QuerysetDispatcher.get_queryset_req("cet6")
        self.assertEqual(qs6.model, Cet6WordsReqModelSerializer.Meta.model)
        qs8 = QuerysetDispatcher.get_queryset_req("neep")
        self.assertEqual(qs8.model, NeepWordsReqModelSerializer.Meta.model)

    def test_get_queryset_study(self):
        qs4 = QuerysetDispatcher.get_queryset_study("cet4")
        self.assertEqual(qs4.model, Cet4StudyModelSerializer.Meta.model)
        qs6 = QuerysetDispatcher.get_queryset_study("cet6")
        self.assertEqual(qs6.model, Cet6StudyModelSerializer.Meta.model)
        qs8 = QuerysetDispatcher.get_queryset_study("neep")
        self.assertEqual(qs8.model, NeepStudyModelSerializer.Meta.model)
