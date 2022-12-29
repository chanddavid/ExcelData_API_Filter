# from .models import Location, Project, Helper, Doner, Budget, Sector
from .models import ExcelData
from rest_framework import serializers


class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelData
        fields = '__all__'


# class LocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Location
#         fields = '__all__'


# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'


# class HelperSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Helper
#         fields = '__all__'


# class DonerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Doner
#         fields = '__all__'


# class BudgetnSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Budget
#         fields = '__all__'


# class SectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sector
#         fields = '__all__'
