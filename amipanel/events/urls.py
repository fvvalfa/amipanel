from django.urls import path
from .views import *
urlpatterns = [
    path('', get_events_by_date, name='get_events_by_date'),
    path('<int:year>/<int:month>/<int:day>/', get_events_by_date, name='get_events_by_date'),

# ?year=2022&month=6&day=19
]