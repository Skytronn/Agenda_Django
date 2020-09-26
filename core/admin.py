from django.contrib import admin
from core.models import Evento
#registro de classes da model

#adiciona as colunas para o objeto no django admin, com as colunas informadas
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'data_evento', 'data_criacao', 'usuario')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin)