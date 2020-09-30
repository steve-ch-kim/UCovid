from django.db import models

# Create your models here.

class California(models.Model):
    total_cases = models.PositiveIntegerField()
    new_cases = models.PositiveIntegerField(default=0)
    total_deaths = models.PositiveIntegerField()
    new_deaths = models.PositiveIntegerField(default=0)
    total_tests = models.PositiveIntegerField()

    def __str__(self):
        return 'California Total'

class College(models.Model):
    college_name = models.CharField(max_length=200)
    college_total_cases = models.PositiveIntegerField(null=True, blank=True)
    county_name = models.CharField(max_length=200)
    county_total_cases = models.PositiveIntegerField()
    county_new_cases = models.PositiveIntegerField(default=0)
    county_total_deaths = models.PositiveIntegerField()
    county_active_cases = models.TextField(default='N/A')
    county_total_tests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.college_name}"
