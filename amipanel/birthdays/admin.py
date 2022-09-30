from datetime import datetime

from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django import forms 
from django.forms import DateField
from .models import Department, birthday
from django.shortcuts import render
from django.urls import path, reverse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django.utils.html import format_html
# Register your models here.
from django.utils import timezone
from django.contrib import admin, messages
from .models import birthday


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

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
   

class birthdayAdmin(admin.ModelAdmin):
    list_display = ('day', 'name', 'department', 'photo_url')
    list_filter = (('day', DateRangeFilter), ('day', DateFieldListFilter),)
    
    readonly_fields = ('photo_url',)

    def image_tag(self, obj):
        from django.utils.html import escape
        data = format_html('<img src="%s" />' % escape(obj.photo.url))
        return data if data!=None else ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def get_urls(self) :
        urls = super().get_urls()
        new_urls = [path('upload_csv/', self.upload_csv)]
        return new_urls+urls

    def upload_csv(self, request):
        if request.method =="POST":
            process_line=0
            csv_file = request.FILES['csv_upload']
            file_data = csv_file.read().decode('utf-8-sig')
            csv_data = file_data.replace('\r','').split('\n')
            for item in csv_data:
                process_line=process_line+1
                fields = item.split(';')
                if len(fields)<4:
                    continue
                try:
                    field_day = datetime.strptime(fields[0], '%d.%m.%Y')
                    field_name = fields[1]
                    field_birthdaywishes = fields[2]
                    filed_department= fields[3]
                    field_photo= fields[4]
                except ValueError:
                    field_day = None
                    field_name = None
                    field_birthdaywishes = None
                    filed_department= None
                    field_photo= None
                    messages.warning(request,'Ошибка при обработке файла. Строка номер - {0}. Формат файла - Дата(день.месяц.год);ФИО;Пожелания;Подразделение;'.format(process_line))
                    return HttpResponseRedirect(request.path_info)
                if field_day == None or field_name == None:
                    break
                values_for_update={'day':field_day}
                if field_birthdaywishes != '' and field_birthdaywishes!=None:
                    values_for_update.update({'birthdaywishes':field_birthdaywishes})
                if filed_department != '' and filed_department!=None:
                    depart, created = Department.objects.get_or_create(title=filed_department)
                    values_for_update.update({'department':depart})
                if field_photo != '' and field_photo!=None:
                    values_for_update.update({'photo':field_photo})
                #values_for_update={'day':field_day, "birthdaywishes": field_birthdaywishes, 'department':filed_department, 'photo':field_photo}
                created = birthday.objects.update_or_create(
                    name = field_name,
                    defaults=values_for_update
                )

            url = reverse('admin:birthdays_birthday_changelist')
            return HttpResponseRedirect(url)
        form=CsvImportForm()
        data={'form': form}
        
        return render(request, 'admin/csv_upload.html', data)


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

admin.site.register(birthday, birthdayAdmin)
admin.site.register(Department, DepartmentAdmin)


