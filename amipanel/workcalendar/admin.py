from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.forms import DateField
from .models import CalendarDays
# Register your models here.

class CalendarDayAdmin(admin.ModelAdmin):
    list_display=('day', 'hours', 'day_of_the_week')
    list_filter = (
        ('day', DateFieldListFilter),
    )
    list_editable = ('hours',)
 
#  инициализация значение в поле часы 
    def get_form(self, request, obj=None, **kwargs):
        form = super(CalendarDayAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['hours'].initial = 8
        return form

admin.site.register(CalendarDays, CalendarDayAdmin)
