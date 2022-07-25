from pyexpat import model
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Events(models.Model):
    start_event = models.DateTimeField('Начало события')
    duration = models.IntegerField('Продолжительность')
    event_name = models.CharField('Событие', max_length=150)
    
    
    class Meta():
        db_table='events'
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['start_event']

    def get_events_by_date(self, year, month, day):
        try:
            eventvalue = Events.objects.filter(
                start_event__year=year,start_event__month=month, start_event__day=day)
        except ObjectDoesNotExist:
            eventvalue = None
        print(eventvalue)
        return eventvalue
        
