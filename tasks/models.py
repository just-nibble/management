import datetime
from django.db import models
from employees.models import Employee
# Create your models here.


class Task(models.Model):
    state = [
        ("pending", "pending"), ("assigned", "assigned"),
        ("incomplete", "incomplete"), ("complete", "complete")
    ]

    task_name = models.CharField(max_length=300, verbose_name="task name")
    assigned_by = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        verbose_name="assigned by"
    )
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        verbose_name="assigned to"
    )
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_completed = models.CharField(max_length=300)
    status = models.CharField(choices=state, max_length=20, default="pending")

    def get_date_completed(self):
        if self.status == "complete":
            self.date_completed = datetime.day.today()

    def save(self, *args, **kwargs):
        self.get_date_completed()
        super(Task, self).save(*args, **kwargs)
