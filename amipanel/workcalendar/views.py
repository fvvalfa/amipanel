import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render

from .HTTPWorkCalendar.httpworkcalendar import HTTPWorkCalendar

# Create your views here.

def get_calendar(request):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)

    if year is not None and year.isnumeric():
        year = int(year)
    if month is not None and month.isnumeric():
        month = int(month)
    
    cal = HTTPWorkCalendar()
#    cal = HTMLCalendar()
    cal.cssclass_month_head="month_head"
    if year ==None:
        year = datetime.datetime.now().year
    if month ==None:
        month = datetime.datetime.now().month
    

    calResult= cal.formatmonth(theyear=year, themonth = month,withyear=True)
    return HttpResponse(calResult)

