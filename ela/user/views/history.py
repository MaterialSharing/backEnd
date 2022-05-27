from rest_framework.viewsets import ModelViewSet

from cxxulib.static_values import wshob
from user.serializer import WSHModelSerializer
from rest_framework.viewsets import ModelViewSet

from user.serializer import WSHModelSerializer


class WSHModelViewSet(ModelViewSet):
    queryset = wshob.all()
    serializer_class = WSHModelSerializer
    filter_fields = ["spelling", "user"]
    search_fields = ['spelling', "user"]

    def history_create(self, req):
        """post:create a entry for user search a warod"""
        return self.create(req)
