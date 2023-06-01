from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    reg_number = models.CharField(max_length=10, db_index=True)
    id_number = models.CharField(max_length=10, db_index=True)
    system_designation = models.ForeignKey('SystemDesignation', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{} {} - {} - {}".format(self.first_name, self.last_name, self.reg_number, str(self.system_designation))


class Region(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class County(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Counties'

    def __str__(self):
        return self.title


class SubCounty(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'SubCounty'
        verbose_name_plural = 'SubCounties'

    def __str__(self):
        return self.title


class Station(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    code = models.BigIntegerField(default=0, blank=True, null=True)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.title


class Directorate(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class DirectorateDivision(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)
    directorate = models.ForeignKey(Directorate, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.title


class ReportingType(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class SystemDesignation(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title


class HrDesignation(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)
    system_designation = models.ForeignKey(SystemDesignation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class SystemDesignationMapping(models.Model):
    system_designation = models.ForeignKey(SystemDesignation, on_delete=models.CASCADE, blank=True, null=True)
    reporting_to = models.ForeignKey(SystemDesignation, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='reporting_to')
    reporting_type = models.ForeignKey(ReportingType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(str(self.system_designation), str(self.reporting_to), str(self.reporting_type))


class LeaveType(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)
    code = models.IntegerField(default=0, blank=True, null=True)
    entitlement = models.IntegerField(default=0, blank=True, null=True)
    max_to_take = models.IntegerField(default=0, blank=True, null=True)
    carry_over_limit = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return "{}  - ({})".format(self.title, self.entitlement)


class Quarter(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True, db_index=True)

    def __str__(self):
        return self.title


class QuarterSetup(models.Model):
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, blank=True, null=True, db_index=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "{} - ({}) - ({})".format(self.quarter, self.start_date, self.end_date)
