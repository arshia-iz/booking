from django.db import models
from accounts.models import User
# Create your models here.
class Reservation (models.Model):
    status = (
        ("pending","pending"),
        ("confirmed","confirmed"),
        ("canceled","canceled"),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey("service.Service", on_delete=models.CASCADE)
    time_slot = models.ForeignKey("timeslot.Timeslot" , on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=status,default="pending")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)