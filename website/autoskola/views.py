from django.http import HttpResponse
from django.template import loader

from autoskola.models import Otazka

def index(request):
    questions = Otazka.objects.all()
    template = loader.get_template('index.html')
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))