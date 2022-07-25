import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render

from .models import Events


def get_events_by_date(request):
    events = Events()
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    day = request.GET.get('day', None)
    events = events.get_events_by_date(year, month, day)
    if events.count()==0:
        return HttpResponse('<div> Сегодня нет событий </div>')
    
    events_results = []
    add = events_results.append
    eventitem:Events

    for eventitem in events:
        add('<div class="%s">'%('birthday_card'))
        add('<div class={}> {:%H-%M} </div>'.format('birthday_day', eventitem.start_event))
        add('<div class="%s"> %s </div>'%('birthday_name', eventitem.event_name))
        add('<div class="%s"> %s </div>'%('birthday_name', eventitem.duration))
        add('</div>')
    return HttpResponse(''.join(events_results))

    