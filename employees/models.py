from django.db import models
import datetime
# Create your models here.


class Employee(models.Model):
    picture = models.ImageField(upload_to="profile_pictures")
    first_name = models.CharField(max_length=50, verbose_name="first name")
    last_name = models.CharField(max_length=50, verbose_name="last_name")
    date_of_birth = models.DateField(verbose_name="date of birth")
    age = models.CharField(max_length=3, verbose_name="age")

    def find_age(self):
        self.age = datetime.date.today() - self.date_of_birth

    def save(self, *args, **kwargs):
        self.find_age()
        super(Employee, self).save(*args, **kwargs)
