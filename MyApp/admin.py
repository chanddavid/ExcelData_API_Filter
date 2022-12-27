from django.contrib import admin
from .models import Location, Project, Helper, Doner, Budget, Sector
# Register your models here.

admin.site.register(Location)
admin.site.register(Project)
admin.site.register(Helper)
admin.site.register(Doner)
admin.site.register(Budget)
admin.site.register(Sector)
