from rest_framework import mixins
from rest_framework import generics
import json
from rest_framework.response import Response

class TestView(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return_data = {
            'code': "yo get something"
        }
        return Response(return_data)

    def post(self, request, *args, **kwargs):
        return_data = {
            'code': "yo post something"
        }
        return Response(return_data)

    def put(self, request, *args, **kwargs):
        return_data = {
            'code': "yo put something"
        }
        return Response(return_data)

    def delete(self, request, *args, **kwargs):
        return_data = {
            'code': "yo delete something"
        }
        return Response(return_data)