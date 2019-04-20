from django.db import models
from common.models import Log_template

# Create your models here.
class Perf_log_report(models.Model):
    log_details = models.ForeignKey(Log_template,on_delete=models.CASCADE)
    report_png = models.ImageField(name="Perf_log_{0}_{1}.png".format(Log_template.machine,Log_template.date_upload),unique=True)
