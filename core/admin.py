from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','data_evento','data_criacao')
    list_filter = ('titulo','usuario','data_evento','local',)

admin.site.register(Evento, EventoAdmin)

#lembrar de fazer python manage.py migrate core 0001
# ou sqlmigrate