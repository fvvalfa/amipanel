import datetime
import locale
from django.http import HttpResponse
from django.shortcuts import render
from pkg_resources import require
from django.http import JsonResponse
from .models import Needreload


def do_needreload(request):
    req = Needreload()
    req = req.do_need_reload()
    req:Needreload
    return JsonResponse({'required_reload':req.required})
    

def needreload(request, reload_site_value):
    req = Needreload()
    req = req.set_need_reload(reload_site_value)
    return JsonResponse({'needreloadset':req})

    
