from django.contrib import admin

from .models import birthday

class birthdayAdmin(admin.ModelAdmin):
    list_display = ('day', 'name', 'department')

admin.site.register(birthday, birthdayAdmin)

