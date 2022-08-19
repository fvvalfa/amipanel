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
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django.utils.html import format_html
# Register your models here.
from django.utils import timezone


class CsvImportForm(forms.Form):
    '''Форма для выбора файла с атрибутом только CSV'''
    csv_upload = forms.FileField(label='Выберите файл для загрузки',
        widget=forms.ClearableFileInput(
            attrs={
                'accept':".csv",
                'class': 'send_file_button'
                }
            )
        )
    

class CalendarDayAdmin(admin.ModelAdmin):
    list_display=('day', 'hours', 'day_of_the_week')
    list_filter = (('day', DateRangeFilter), )

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
        return render(request, 'admin/csv_upload.html', data)

#  инициализация значение в поле часы 
    def get_form(self, request, obj=None, **kwargs):
        form = super(CalendarDayAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['hours'].initial = 8
        return form


    # If you would like to add a default range filter
    # method pattern "get_rangefilter_{field_name}_default"
    def get_rangefilter_day_default(self, request):
        now = timezone.now()
        date=now.date()
        return (date, date)

    # If you would like to change a title range filter
    # method pattern "get_rangefilter_{field_name}_title"
    # def get_rangefilter_day_title(self, request, field_path):
    #     return 'custom title'

admin.site.register(CalendarDays, CalendarDayAdmin)



