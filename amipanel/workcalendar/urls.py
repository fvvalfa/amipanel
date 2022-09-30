from django.urls import path
from .views import *
urlpatterns = [
    path('', get_calendar, name='get_calendar'),
    #path('<int:year>/<int:month>/', get_calendar, name='get_calendar'),
 
]
