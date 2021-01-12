from django.db import models
from employees.models import Employee
# Create your models here.


class TaskReport(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE
    )
    number_of_pending = models.IntegerField(
        verbose_name="number of pending"
    )
    number_of_assigned = models.IntegerField(
        verbose_name="number of assigned"
    )
    number_of_incomplete = models.IntegerField(
        verbose_name="number of incomplete"
    )
    number_of_completed = models.IntegerField(
        verbose_name="number of completed"
    )

    def __str__(self):
        return str(self.employee__first_name) + " work report"


'''
    def get_pending(self):
        pending_tasks = Employee.objects.filter(status == "pending")

    def get_assigned(self):
        pending_tasks = Employee.objects.filter(status == "pending")

    def get_incomplete(self):
        pending_tasks = Employee.objects.filter(status == "pending")

    def get_completed(self):
        pending_tasks = Employee.objects.filter(status == "pending")

    def save(self, *args, **kwargs):
        self.get_date_completed()
        super(Task, self).save(*args, **kwargs)
'''
