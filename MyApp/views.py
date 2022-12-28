from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.db import IntegrityError

from .models import ExcelData


class DataView(APIView):
    def get(self, request, id=None):
        pass

    def post(self, request):
        data = request.data

        dataframe1 = pd.read_excel(data['filename'], header=[0])
        dataframe1.columns = dataframe1.columns.str.replace(' ', '')
        for i in dataframe1.itertuples():
            try:
                obj1 = ExcelData.objects.create(
                    project_title=i.ProjectTitle, project_status=i.ProjectStatus, humanitarian=i.Humanitarian)
                obj1.save()
            except IntegrityError:
                pass


        return Response({"msg": "successfully created"}, status=status.HTTP_201_CREATED)
        # serializer=Serializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"msg":"successfully Post"},serializer.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors)

    def put(self, request, id=None):
        pass

    def patch(self, request, id=None):
        pass

    def delete(self, request, id=None):
        pass












































# from .models import Location, Project, Helper, Doner, Budget, Sector

# Create your views here.


# class DataView(APIView):
#     def get(self, request, id=None):
#         pass

#     def post(self, request):
#         data = request.data
#         try:
#             ln=Project.objects.all().count()
#         except:
#             pass
        

#         dataframe1 = pd.read_excel(data['filename'], header=[0])
#         for i in dataframe1.itertuples():
#             try:
             
#                 obj1 = Project.objects.create(
#                     project_title=i.ProjectTitle, project_status=i.ProjectStatus, humanitarian=i.Humanitarian)
#                 obj1.save()
 
#                 obj2 = Doner.objects.create(
#                     donar=i.Donor, executing_agency=i.ExecutingAgency, implementing_partner=i.ImplementinPartner, counterpart_ministry=i.CounterpartMinistry, type_of_assistance_code=i.TypeofAssistanceCode)
#                 obj2.save()
        
                
#             except IntegrityError:
#                 pass

        
#         def LocationFunction():
#             try:
#                 for i in dataframe1.itertuples():
#                     for j in range(1, ln+1):
#                         obj3=Location.objects.create(
#                             project=Project.objects.get(project_id=j), province=i.Province, district=i.District, municipality=i.Municipality)
#                         obj3.save()
#             except IntegrityError:
#                 pass
#         LocationFunction()

#         return Response({"msg": "successfully created"}, status=status.HTTP_201_CREATED)
#         # serializer=Serializer(data=data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response({"msg":"successfully Post"},serializer.data,status=status.HTTP_201_CREATED)
#         # else:
#         #     return Response(serializer.errors)

#     def put(self, request, id=None):
#         pass

#     def patch(self, request, id=None):
#         pass

#     def delete(self, request, id=None):
#         pass
