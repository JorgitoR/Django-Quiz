from django.db import models

class Pregunta(models.Model):

	texto = models.TextField(verbose_name='Texto de la pregunta')

	def __str__(self):
		return self.texto 


class ElegirRespuesta(models.Model):

	MAXIMO_RESPUESTA = 4

	pregunta = models.ForeignKey(Pregunta, related_name='preguntas', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='¿Es esta la pregunta correcta?', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')


	def __str__(self):
		return self.texto