from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DataView(APIView):
    def get(self,request,id=None):
        pass

    def post(self, request):
        data=request.data
        serializer=Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def put(self, request,id=None):
        pass

    def patch(self, request,id=None):
        pass

    def delete(self, request,id=None):
        pass
