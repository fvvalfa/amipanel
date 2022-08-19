from django.contrib import admin
from .models import Events
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class EventsAdmin(admin.ModelAdmin):
    list_display = ('start_event', 'stop_event','duration', 'event_name', 'important')
    list_editable = ('important',)
    list_filter = (('start_event', DateRangeFilter),)
admin.site.register(Events, EventsAdmin)

