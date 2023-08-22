from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='dbdemo1_employee'
        verbose_name_plural='Employees'
