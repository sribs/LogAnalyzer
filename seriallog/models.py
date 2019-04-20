from django.db import models
from common.models import Log_template
# Create your models here.

class Serial_Error_keywords(models.Model):
    keyword = models.CharField(max_length=255,unique=True)
    Problem = models.CharField(max_length=80)

class Serial_log_report(models.Model):
    log_details = models.ForeignKey(Log_template,on_delete=models.CASCADE)
    err_keyword = models.ForeignKey(Serial_Error_keywords,on_delete=models.CASCADE)