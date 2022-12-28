from django.db import models

# Create your models here.


class ExcelData(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    municipality = models.CharField(max_length=200)
    project_title = models.CharField(max_length=200, unique=True)
    project_status = models.CharField(max_length=200)
    donar = models.CharField(max_length=200)
    executing_agency = models.CharField(max_length=200)
    implementing_partner = models.CharField(max_length=200, unique=True)
    counterpart_ministry = models.CharField(max_length=200)
    type_of_assistance_code = models.IntegerField()
    budget_type = models.CharField(max_length=200)
    humanitarian = models.CharField(max_length=200)
    sector_name = models.CharField(max_length=200, unique=True)
    sector_code = models.IntegerField()
    commitments = models.IntegerField()
    Aggrement_date = models.DateTimeField()
    date_of_effectiveness = models.DateTimeField()

    def __str__(self):
        return str(self.location_id)








# class Project(models.Model):
#     project_id = models.AutoField(primary_key=True)
#     project_title = models.CharField(max_length=200, unique=True)
#     # remove choice field since we are uploading data from excel file
#     project_status = models.CharField(max_length=200)
#     humanitarian = models.CharField(max_length=200)

#     def __str__(self):
#         return self.project_title


# class Location(models.Model):
#     location_id = models.AutoField(primary_key=True)
#     # one project have many location just as in Dat
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     province = models.CharField(max_length=200)
#     district = models.CharField(max_length=200)
#     municipality = models.CharField(max_length=200)

#     def __str__(self):
#         return str(self.location_id)


# class Doner(models.Model):
#     doner_id = models.AutoField(primary_key=True)
#     donar = models.CharField(max_length=200)
#     executing_agency = models.CharField(max_length=200)
#     implementing_partner = models.CharField(max_length=200, unique=True)
#     counterpart_ministry = models.CharField(max_length=200)
#     type_of_assistance_code = models.IntegerField()

#     def __str__(self):
#         return str(self.doner_id)


# class Helper(models.Model):
#     helper_id = models.AutoField(primary_key=True)
#     doner_id = models.ForeignKey(Doner, on_delete=models.CASCADE)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.helper_id)


# class Budget(models.Model):
#     budget_id = models.AutoField(primary_key=True)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
#     budget_type = models.CharField(max_length=200)
#     commitments = models.IntegerField()
#     Aggrement_date = models.DateTimeField()
#     date_of_effectiveness = models.DateTimeField()

#     def __str__(self):
#         return str(self.budget_id)


# class Sector(models.Model):
#     sector_id = models.AutoField(primary_key=True)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
#     sector_name = models.CharField(max_length=200, unique=True)
#     sector_code = models.IntegerField()

#     def __str__(self):
#         return self.sector_name


# *-*-*-*-*_*_*_*______**_*_*_*_*_*_*_


# # Create your models here.

# BUDGET_STATUS = (
#     ("On-Going", "On-Going"),
#     ("Pending", "Pending"),
#     ("Completed", "Completed"),
#     ("Cancled", "Cancled")
# )

# HUMANITARIAN = (
#     ("Yes", "Yes"),
#     ("No", "No")
# )


# class Project(models.Model):
#     project_id = models.AutoField(primary_key=True)
#     project_title = models.CharField(max_length=200, unique=True)
#     #remove choice field since we are uploading data from excel file
#     project_status = models.CharField(max_length=200, choices=BUDGET_STATUS)
#     humanitarian = models.CharField(max_length=200, choices=HUMANITARIAN)

#     def __str__(self):
#         return self.project_title


# class Location(models.Model):
#     location_id = models.AutoField(primary_key=True)
#     # one project have many location just as in Dat
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     province = models.CharField(max_length=200, unique=True)
#     district = models.CharField(max_length=200, unique=True)
#     municipality = models.CharField(max_length=200, unique=True)

#     def __str__(self):
#         return str(self.location_id)


# class Doner(models.Model):
#     doner_id = models.AutoField(primary_key=True)
#     donar = models.CharField(max_length=200)
#     executing_agency = models.CharField(max_length=200)
#     implementing_partner = models.CharField(max_length=200, unique=True)
#     counterpart_ministry = models.CharField(max_length=200)
#     type_of_assistance_code = models.IntegerField()

#     def __str__(self):
#         return str(self.doner_id)


# class Helper(models.Model):
#     helper_id = models.AutoField(primary_key=True)
#     doner_id = models.ForeignKey(Doner, on_delete=models.CASCADE)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.helper_id)


# BUDGET_TYPE = (
#     ("On Budget", "On Budget"),
#     ("Off Budget", "Off Budget"),
# )


# class Budget(models.Model):
#     budget_id = models.AutoField(primary_key=True)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
#     budget_type = models.CharField(max_length=200, choices=BUDGET_TYPE)
#     #helper_id=models.ForeignKey(Helper,on_delete=models.CASCADE)
#     commitments = models.IntegerField()
#     Aggrement_date = models.DateTimeField()
#     date_of_effectiveness = models.DateTimeField()

#     def __str__(self):
#         return str(self.budget_id)


# class Sector(models.Model):
#     sector_id = models.AutoField(primary_key=True)
#     project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
#     sector_name = models.CharField(max_length=200)
#     sector_code = models.IntegerField()

#     def __str__(self):
#         return self.sector_name



