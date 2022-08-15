"""amipanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from amipanel.views import show_home_page
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home_page),
    path('get_calendar/', include('workcalendar.urls')),
    path('get_birthdays/', include('birthdays.urls')),
    path('get_events_by_date/', include('events.urls')),
    path('needreload/', include('needreload.urls')),
    path('weather/', include('weather.urls')),
    #path('reloadconfirm/', include('needreload.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

