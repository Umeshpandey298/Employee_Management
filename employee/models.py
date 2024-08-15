from django.db import models

# Create your models here.

class Employee(models.Model):
  name=models.CharField(max_length=100,null=False)
  emp_id=models.IntegerField(null=False)
  phone=models.IntegerField()
  address=models.CharField(max_length=100,null=False)
  working=models.BooleanField(default=True)
  department=models.CharField(max_length=100)

  def __str__(self):
    return self.name



