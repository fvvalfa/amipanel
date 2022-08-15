from pyexpat import model
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class birthday(models.Model):
    day = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=150,verbose_name='ФИО')
    birthdaywishes = models.CharField(max_length=150,\
     blank=True,\
     verbose_name='Пожелания',\
     default="С днем рождения! Пусть мечты сбываются, счастье не заканчивается, удача не покидает, а близкие всегда будут рядом.")
    department = models.CharField(max_length=150,verbose_name='Подразделение', blank=True)
    photo = models.ImageField(verbose_name='Фото',blank=True,upload_to="photo/")

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
