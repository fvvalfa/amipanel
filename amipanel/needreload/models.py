import datetime
from gettext import translation
from hashlib import new
from importlib.metadata import requires
from pyexpat import model
import re
from time import timezone
from tracemalloc import start
from django.db.models import Q,F,ExpressionWrapper
from django.db import models, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.forms import DurationField
from django.utils import timezone
from django.test import TransactionTestCase
from pkg_resources import require

class Needreload(models.Model):
    required = models.IntegerField('Требуется перезагрузка', default=False)
 #   started = models.DateTimeField('Начало', auto_now=True)
#    ended = models.DateTimeField('Конец')
    
    class Meta():
        db_table='need_reload'
        verbose_name = "Нужна перезагрузка"
        verbose_name_plural = "Нужна перезагрузка"

    def do_need_reload(self):
#        now = datetime.datetime.now()
        now = timezone.now()
        required=Needreload()
        try:
            required = Needreload.objects.get()
            # if required.required==True:
            #     required.required=False
            #     required.save()
        except ObjectDoesNotExist:
            required.required = False
        # print(eventvalue)
        return required
        
    def set_need_reload(self, reload_site_value):
        '''Установка признака для перезагрузки страницы сайта'''
        
        #now = datetime.datetime.now()
        now = timezone.now()
        required_field=False
        #with transaction.atomic():
        eventvalue = False
        with transaction.atomic():
            try:
                required_field: Needreload
                required_field, created  = Needreload.objects.get_or_create()
                #filter(Q(started__lte=now) & Q(ended__gte=now)).
                # required_field.ended= datetime.date(9999,12,31)
                required_field.required=reload_site_value
                required_field.save()
                eventvalue=True
            except ObjectDoesNotExist:
                eventvalue = False
            # print(eventvalue)
        return eventvalue

        
