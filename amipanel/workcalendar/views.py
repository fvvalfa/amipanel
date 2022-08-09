import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render

from .HTTPWorkCalendar.httpworkcalendar import HTTPWorkCalendar

# Create your views here.

def get_calendar(request):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    cal = HTTPWorkCalendar()
#    cal = HTMLCalendar()
    cal.cssclass_month_head="month_head"
    calResult= cal.formatmonth(theyear=datetime.datetime.now().year, themonth=datetime.datetime.now().month,withyear=True)
    return HttpResponse(calResult)