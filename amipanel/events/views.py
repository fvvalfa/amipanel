import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render

from .models import Events


def get_events_http_by_date(request):
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
        add('<div class={}> {:%H:%M}-{:%H:%M}</div>'.format('birthday_day', eventitem.start_event,  eventitem.start_event+datetime.timedelta(minutes=eventitem.duration)))
        add('<div class="%s"> %s </div>'%('birthday_name', eventitem.event_name))
        add('<div class="%s"> %s </div>'%('birthday_name', eventitem.duration))
        add('</div>')
    return HttpResponse(''.join(events_results))

def get_events_by_date(request):
    events = Events()
    year = request.GET.get('year', 0)
    month = request.GET.get('month', 0)
    day = request.GET.get('day', 0)
    events = events.get_events_by_date(int(year), int(month), int(day))
    # if events.count()==0:
    #     return HttpResponse('<div> Сегодня нет событий </div>')
    
    # events_results = []
    # add = events_results.append
    # eventitem:Events
    

    # for eventitem in events:
    #     events_results.append(
    #         {
    #             'start_event':eventitem.start_event,
    #             'stop_event':eventitem.start_event+datetime.timedelta(minutes=eventitem.duration),
    #             'event_name':eventitem.event_name
    #      }
    #      )
        
    #    {'pre_eventvalue':pre_eventvalue,'cur_eventvalue':cur_eventvalue,'next_eventvalue':next_eventvalue }
    context =  {'pre_eventvalue':events['pre_eventvalue'],'cur_eventvalue':events['cur_eventvalue'],'next_eventvalue':events['next_eventvalue'] }
    return render(request, 'events/events.html', context)
    # return render(request, 'events/events.html', {'events':events })

    