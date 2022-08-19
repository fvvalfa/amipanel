import datetime
from pyexpat import model
from django.utils import timezone
from django.db.models import Q,F,ExpressionWrapper
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.forms import DurationField

class Events(models.Model):
    start_event = models.DateTimeField('Начало события')
    #stop_event = models.DateTimeField('Окончание события', null=True)
    duration = models.DurationField('Продолжительность', null=True, help_text='Формат- Часы:Минуты:Секунды')
    event_name = models.CharField('Событие', max_length=150)
    important = models.BooleanField('Важное событие', default=False)
    
    
    @property
    def stop_event(self):
        value=self.start_event+self.duration
        return value
    def __str__(self):
        return self.event_name
    
    
    class Meta():
        db_table='events'
        verbose_name = "Событие"
        verbose_name_plural = "События"
        ordering = ['start_event']
    #stop_event.short_description = 'Окончание события'

    def get_events_by_date(self):
        now = timezone.now()
        date=now.date()
        try:
            #Поиск прошедших событий 
            pre_eventvalue = Events.objects.annotate(stop_event_calc=ExpressionWrapper(F('start_event')+F('duration'), output_field=models.DateTimeField())).filter(Q(start_event__date=date)).filter(stop_event_calc__lt=now)
            print(pre_eventvalue)
            #Поиск текущих событий
            cur_eventvalue = Events.objects.\
            annotate(stop_event_calc=ExpressionWrapper(F('start_event')+F('duration'), output_field=models.DateTimeField())).\
            filter(Q(start_event__date=date)&Q(start_event__lte = now)&Q(stop_event_calc__gte=now))
            print(cur_eventvalue)
            #Поиск будущих событий
            next_eventvalue = Events.objects.filter(Q(start_event__date=date)&Q(start_event__gt = now))
            print(now.time())
            print(next_eventvalue)
            print(pre_eventvalue.count())
            print(cur_eventvalue.count())
            print(next_eventvalue.count())
        except ObjectDoesNotExist:
            eventvalue = None
        # print(eventvalue)
        return {'pre_eventvalue':pre_eventvalue,'cur_eventvalue':cur_eventvalue,'next_eventvalue':next_eventvalue }
        
