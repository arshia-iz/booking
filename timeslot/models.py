from django.db import models

# Create your models here.
class Timeslot (models.Model):
    service = models.ForeignKey("service.Service", on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField()