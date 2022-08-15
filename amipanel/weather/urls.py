from django.urls import path
from .views import *
urlpatterns = [
    path('', get_current_weather, name='weather'),
    #path('<int:year>/<int:month>/<int:day>/', get_all_birthdays, name='get_all_birthdays'),

# ?year=2022&month=6&day=19
]
