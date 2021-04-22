Video #9

En este video vamos a desarrollar funciones a nuestro aplicativo, Obtener las nuevas
preguntas desarrolladas a nuestro Quiz, excluir las que ya hemos respondido,


```python

  
  def crear_intentos(self, pregunta):
    intento = PreguntasRespondidas(pregunta=pregunta, quizUser=self)
    intento.save()

  def obtener_nuevas_preguntas(self):
    respondidas = PreguntasRespondidas.objects.filter(quizUser=self).values_list('pregunta__pk', flat=True)
    preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
    if not preguntas_restantes.exists():
      return None
    return random.choice(preguntas_restantes)

  def validar_intentos(self, pregunta_respondida, respuesta_selecionada):

    if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
      return 


    pregunta_respondida.respuesta_selecionada = respuesta_selecionada
    if respuesta_selecionada.correcta is True:
      pregunta_respondida.correcta = True
      pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
    pregunta_respondida.save()

```




