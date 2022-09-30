from cProfile import label
from html import escape
from pyexpat import model
from django.db import models
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.utils.html import format_html


class Department(models.Model):
    title = models.CharField(max_length=150,verbose_name='Подразделение', blank=True)
    def __str__(self):
        return self.title
    class Meta():
        db_table='Departments'
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"
        ordering = ['title']



class birthday(models.Model):
    day = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=150,verbose_name='ФИО')
    birthdaywishes = models.CharField(max_length=150,\
     blank=True,\
     verbose_name='Пожелания',\
     default="С днем рождения! Пусть мечты сбываются, счастье не заканчивается, удача не покидает, а близкие всегда будут рядом.")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True)
    photo = models.ImageField(verbose_name='Фото',blank=True,upload_to="photo/", help_text='Размер фото 185х250')
    def __str__(self):
        return self.name


    @property
    @admin.display(description='Предпросмотр')
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return  format_html('<img class ="preview_image" src="%s" />' % escape(self.photo.url))
        else:
            return format_html('')
            

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
