from django.db import models

# Create your models here.
from django.db import models
class File(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  student_id=models.CharField(max_length=15)
  timestamp = models.DateTimeField(auto_now_add=True)