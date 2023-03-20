from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Eleccion, Pregunta

def index(request):
    ultimasPreguntas = Pregunta.objects.order_by('-fechaPublicacion')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'ultimasPreguntas': ultimasPreguntas,
    }
    return HttpResponse(template.render(context, request))

def detalles(request, pregunta_id):
    try:
        pregunta = Pregunta.objects.get(pk=pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404("La encuesta no existe")
    return render(request, 'polls/detalles.html', {'pregunta': pregunta})

def resultados(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render(request, 'polls/resultados.html', {'pregunta': pregunta})

def votar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    try:
        selected_eleccion = pregunta.eleccion_set.get(pk=request.POST['eleccion'])
    except (KeyError, Eleccion.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'pregunta': pregunta,
            'error_message': "No has elegido una opción.",
        })
    else:
        selected_eleccion.votos += 1
        selected_eleccion.save()
        return HttpResponseRedirect(reverse('polls:resultados', args=(pregunta.id,)))

