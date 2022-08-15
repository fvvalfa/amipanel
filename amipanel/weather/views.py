import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render
from pyowm.owm import OWM

class Weather_parameters():
    def __init__(self):
        self.city=''
        self.timerequest=0
        self.temperature=0
        self.detailed_status=''
        self.temperaturefeelslike=0
        self.windspeed=0
        self.winddeg=0
        self.humidity=0
        self.icon_name =''
        self.pressure=0
def get_current_weather(request):
    weatherparam = Weather_parameters()
    owm = OWM('abced3e2e83c5b506f7052df18ec09d1')
    owm.config[ "language"]='ru'
    mgr = owm.weather_manager()
    weather = mgr.weather_at_place('Moscow,RU').weather  # get the weather at London,GB now
    weather_dict = mgr.weather_at_place('Moscow,RU').to_dict()
    wind = weather.wind()
    temperature_dict = weather.temperature('celsius')
    
    weatherparam.city= weather_dict['location']['name'] 
    weatherparam.detailed_status = str.capitalize(weather_dict['weather']['detailed_status'])
    
    weatherparam.pressure = weather_dict['weather']['pressure']['press']
    weatherparam.icon_name = weather_dict['weather']['weather_icon_name']
    weatherparam.timerequest =weather_dict['reception_time']
    weatherparam.temperature = round(temperature_dict['temp'],1)
    weatherparam.temperaturefeelslike = round(temperature_dict['feels_like'],1)
    weatherparam.windspeed=wind['speed']
    weatherparam.winddeg=wind['deg']
    
    weatherparam.winddeg=weatherparam.winddeg-180
    weatherparam.humidity = weather.humidity

   

    #weather.weather_icon_name='08d' 
    # context={'temperture': temperature,
    #  'icon':weather.weather_icon_name, 
    #  'detailed_status' :weather.detailed_status,
    #  'wind':wind
    #  }
    
    # weather.weather_icon_name
    # weather.detailed_status



    return render(request, 'weather/weather.html', {'weatherparam':weatherparam}) 
    #render(request, 'birthdays/birthday.html', {'birthdays':birthdays })


# def get_http_birthdays(request, year, month, day):
#     bd = birthday()
#     birthdays = bd.get_all_birthdays(month, day)
#     if birthdays.count()==0:
#         return HttpResponse('<div class = "birthday_nodays"> Сегодня нет дней рождения </div>')
#     birthdayresult = []
#     add = birthdayresult.append
#     birthdayitem:birthday

#     for birthdayitem in birthdays:
#         add('<div class="%s">'%('birthday_card'))
#         add('<div class={}> {:%d-%m-%Y } </div>'.format('birthday_day', birthdayitem.day))
#         add('<div class="%s"> %s </div>'%('birthday_name', birthdayitem.name))
#         add('</div>')
#     return HttpResponse(''.join(birthdayresult))

# def get_all_birthdays(request, year, month, day):
#     bd = birthday()
#     birthdays = bd.get_all_birthdays(month, day)
#     return render(request, 'birthdays/birthday.html', {'birthdays':birthdays })
# def get_all_birthdays(request):

#     bd = birthday()
#     year = request.GET.get('year', None)
#     month = request.GET.get('month', None)
#     day = request.GET.get('day', None)
#     birthdays = bd.get_all_birthdays(month, day)
#     return render(request, 'birthdays/birthday.html', {'birthdays':birthdays })

