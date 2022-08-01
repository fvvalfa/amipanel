from django.contrib import admin

from .models import Events

class EventsAdmin(admin.ModelAdmin):
    list_display = ('start_event', 'stop_event','duration', 'event_name')

admin.site.register(Events, EventsAdmin)

