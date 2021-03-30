from django.contrib import admin

from .models import Pregunta, ElegirRespuesta


class ElegirRespuestaInline(admin.TabularInline):
	model = ElegirRespuesta
	can_delete =False
	max_num = ElegirRespuesta.MAXIMO_RESPUESTA
	min_num = ElegirRespuesta.MAXIMO_RESPUESTA

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)