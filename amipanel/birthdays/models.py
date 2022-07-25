from pyexpat import model
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class birthday(models.Model):
    day = models.DateField()
    name = models.CharField(max_length=150)
    department = models.CharField(max_length=150, blank=True)
    
    class Meta():
        db_table='birthdays'
        verbose_name = "День рождения"
        verbose_name_plural = "Дни рождения"
        ordering = ['day']

    def get_all_birthdays(self, month, day):
        # CalendarDays.objects.filter(
        # Day__year=year, Day__month=month, Day__day=day)
        try:
            bdvalue = birthday.objects.filter(
                day__month=month, day__day=day)
        except ObjectDoesNotExist:
            bdvalue = None
        print(bdvalue)
        return bdvalue
