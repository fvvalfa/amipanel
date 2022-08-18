from ast import Try

from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django import forms 
from django.forms import DateField
from .models import CalendarDays
from django.shortcuts import render
from django.urls import path, reverse
import csv
# Register your models here.


class CsvImportForm(forms.Form):
    '''Форма для выбора файла с атрибутом только CSV'''
    csv_upload = forms.FileField(label='Выберите файл для загрузки',
        widget=forms.ClearableFileInput(
            attrs={
                'accept':".csv",
                }
            )
        )
    

class CalendarDayAdmin(admin.ModelAdmin):
    list_display=('day', 'hours', 'day_of_the_week')
    list_filter = (
        ('day', DateFieldListFilter),
    )
    list_editable = ('hours',)

    def get_urls(self) :
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv)]
        return new_urls+urls

    def upload_csv(self, request):
        if request.method =="POST":
            csv_file = request.FILES['csv_upload']
            file_data = csv_file.read().decode('utf-8-sig')
            csv_data = file_data.replace('\r','').split('\n')
            
            for item in csv_data:
                fields = item.split(';')
                try:
                    field_day = datetime.strptime(fields[0], '%d.%m.%Y')
                    field_hour = fields[1]
                except ValueError:
                    field_day=None
                    field_hour = None
                if field_day == None  or field_hour == None:
                    break
                values_for_update={"day":field_day, "hours": field_hour}
                created = CalendarDays.objects.update_or_create(
                    day = field_day,
                    defaults=values_for_update
                )

            url = reverse('admin:workcalendar_calendardays_changelist')
            return HttpResponseRedirect(url)
        form=CsvImportForm()
        data={'form': form}
        return render(request, 'admin/workcalendar/csv_upload.html', data)

#  инициализация значение в поле часы 
    def get_form(self, request, obj=None, **kwargs):
        form = super(CalendarDayAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['hours'].initial = 8
        return form



admin.site.register(CalendarDays, CalendarDayAdmin)
