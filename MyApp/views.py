from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.db import IntegrityError

from .models import ExcelData
from .serializers import ExcelDataSerializer

import json
from django.db.models import Q


class DataView(APIView):
    def get(self, request, id=None):
        pass

    def post(self, request):
        data = request.data

        dataframe1 = pd.read_excel(data['filename'], header=[0])
        dataframe1.columns = dataframe1.columns.str.replace(' ', '')

        def TimeConvert(lst):
            for i in lst:
                dataframe1[i] = pd.to_datetime(
                    dataframe1[i], format='%m/%d/%Y')
        TimeConvert(['AgreementDate', 'DateofEffectiveness'])
        for i in dataframe1.itertuples():
            obj, created = ExcelData.objects.get_or_create(province=i.Province, district=i.District, municipality=i.Municipality, project_title=i.ProjectTitle, project_status=i.ProjectStatus, donar=i.Donor, executing_agency=i.ExecutingAgency, implementing_partner=i.ImplementingPartner, counterpart_ministry=i.CounterpartMinistry,
                                                           type_of_assistance_code=i.TypeofAssistanceCode, budget_type=i.BudgetType, humanitarian=i.Humanitarian, sector_name=i.Sector, sector_code=i.SectorCode, commitments=i.Commitments, Aggrement_date=i.AgreementDate, date_of_effectiveness=i.DateofEffectiveness)
            if not created:
                #  obj already exists, so skip it
                continue
            obj.save()
        return Response({"msg": "successfully created"}, status=status.HTTP_201_CREATED)

    def put(self, request, id=None):
        pass

    def patch(self, request, id=None):
        pass

    def delete(self, request, id=None):
        pass
# {"sector_name": "Health", "counterpart_ministry": "Ministry of Finance\u00a0", "project_status": "On-Going"}


class GetProjectFilter(APIView):
    def get(self, request):
        data = request.data

        def remove_empty_values(dictionary):
            return {k: v for k, v in dictionary.items() if v}
        data1 = remove_empty_values(data)

        if '' in data.values():
            return Response("please filter by sector_name,counterpart_ministry and project_status with valid value")
        else:
            res1 = ExcelData.objects.filter(
                Q(sector_name=data1["sector_name"]) | Q(counterpart_ministry=data1["counterpart_ministry"]) | Q(project_status=data1["project_status"])).values()
            lst = []
            for i in res1:
                lst.append(i)

            return Response({"msg": lst}, status=status.HTTP_201_CREATED)


class GetSectorFilter(APIView):
    def get(self, request):
        data = ExcelData.objects.all()
        serializer = ExcelDataSerializer(data, many=True)
        data1 = json.dumps(serializer.data)
        print(data1)
        return Response({"msg": serializer.data}, status=status.HTTP_201_CREATED)


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
