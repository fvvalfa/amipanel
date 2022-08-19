import calendar
import locale
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from django.utils.html import format_html
# class NameDay(models.Model):
#     Name = models.CharField(max_length=20)


# class CalendarSettings(models.Model):
#     hourbyday = models.IntegerField()
#     colorday = models.CharField(max_length=10)
#     namesday = models.ForeignKey("NameDay", on_delete=models.CASCADE)




class CalendarDays(models.Model):
    """Список дней с указанием количества часов """
    day = models.DateField(verbose_name='День',unique=True)
    hours = models.IntegerField(verbose_name='Рабочие часы', default=8)
    def __str__(self):
        return self.day.strftime('%d-%m-%Y')

    @property
    @admin.display(description='День недели')
    def day_of_the_week(self):
        # my_date =
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        return ''.join(calendar.day_name[self.day.weekday()])
        

    class Meta():
        db_table='calendardays'
        verbose_name = "День"
        verbose_name_plural = "Дни"
        ordering = ['day']

    def getday(self, year, month, day):
        # CalendarDays.objects.filter(
        # Day__year=year, Day__month=month, Day__day=day)
        try:
            dayvalue = CalendarDays.objects.filter( 
                day__year=year, day__month=month, day__day=day).get()
        except ObjectDoesNotExist:
            dayvalue = None
        return dayvalue

    # def getmonth(self, year, month):
    #     return CalendarDays.objects.filter(Day__year=year, Day__month=month)

    # def getyear(self, year):
    #     return CalendarDays.objects.filter(Day__year=year)
