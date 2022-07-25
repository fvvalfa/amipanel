import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render

from .models import birthday


def get_http_birthdays(request, year, month, day):
    bd = birthday()
    birthdays = bd.get_all_birthdays(month, day)
    if birthdays.count()==0:
        return HttpResponse('<div class = "birthday_nodays"> Сегодня нет дней рождения </div>')
    birthdayresult = []
    add = birthdayresult.append
    birthdayitem:birthday

    for birthdayitem in birthdays:
        add('<div class="%s">'%('birthday_card'))
        add('<div class={}> {:%d-%m-%Y } </div>'.format('birthday_day', birthdayitem.day))
        add('<div class="%s"> %s </div>'%('birthday_name', birthdayitem.name))
        add('</div>')
    return HttpResponse(''.join(birthdayresult))

def get_all_birthdays(request, year, month, day):
    bd = birthday()
    birthdays = bd.get_all_birthdays(month, day)
    return render(request, 'birthdays/birthday.html', {'birthdays':birthdays })
def get_all_birthdays(request):

    bd = birthday()
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    day = request.GET.get('day', None)
    birthdays = bd.get_all_birthdays(month, day)
    return render(request, 'birthdays/birthday.html', {'birthdays':birthdays })
    