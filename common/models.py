from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Linux_details(models.Model):
    machine_distribution_pretty_name = models.CharField(max_length=6)
    machine_kernel_version = models.CharField(max_length=20)
    class Meta:
        unique_together = (("machine_distribution_pretty_name","machine_kernel_version"),)
    
    def __str__(self):
        return self.machine_distribution_pretty_name

class Machine_details(models.Model):
    company_name = models.CharField(max_length=15)
    machine_name = models.CharField(max_length=20)
    machine_os_details = models.ForeignKey(Linux_details,on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(Machine_details.company_name,Machine_details.machine_name)

class Log_template(models.Model):
    machine = models.ForeignKey(Machine_details,on_delete=models.CASCADE)
    filename = models.CharField(max_length=80)
    date_upload = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.filename