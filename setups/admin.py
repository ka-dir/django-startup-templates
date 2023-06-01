from django.contrib import admin
from .models import CustomUser, Region, County, SubCounty, Station, Directorate, DirectorateDivision, SystemDesignation, \
    HrDesignation, LeaveType, Quarter, QuarterSetup, SystemDesignationMapping, ReportingType

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Region)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Station)
admin.site.register(Directorate)
admin.site.register(DirectorateDivision)
admin.site.register(ReportingType)
admin.site.register(SystemDesignation)
admin.site.register(HrDesignation)
admin.site.register(SystemDesignationMapping)
admin.site.register(LeaveType)
admin.site.register(Quarter)
admin.site.register(QuarterSetup)
