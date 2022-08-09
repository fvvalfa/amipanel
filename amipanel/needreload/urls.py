from django.urls import path
from .views import *
urlpatterns = [
    path('get/', do_needreload, name='do_needreload'),
    path('set/<int:reload_site_value>/',needreload, name='needreload'),
    # path('<int:year>/<int:month>/<int:day>/', get_events_by_date, name='get_events_by_date'),

# ?year=2022&month=6&day=19
]