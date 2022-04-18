from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from autoskola.models import Otazka, Odpoved, Zakon, Znacka, Odstavec
from autoskola.forms import OdpovedForm

def index(request):
    questions = Otazka.objects.all()
    template = loader.get_template('index.html')
    context = {
        'questions': questions,
    }
    return HttpResponse(template.render(context, request))

class TestCreate(CreateView):
    model = Odpoved
    success_url = reverse_lazy('odpoved-create')
    form_class = OdpovedForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        otazka = Otazka.objects.order_by('?')[0]
        context["otazka"] = otazka
        return context

def stat(request):
    template = loader.get_template('autoskola/statistics.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def get_data(request):
    otazky = Otazka.objects.all().count()
    odpovedi = Odpoved.objects.all().count()
    znacky = Znacka.objects.all().count()
    odstavce = Odstavec.objects.all().count()
    zakony = Znacka.objects.all().count()

    labels = ['Otázky', 'Odpovědi', 'Značky', 'Odstavce', 'Zákony']
    default = [otazky, odpovedi, znacky, odstavce, zakony]
    data = {
        "labels": labels,
        "default": default,
    }
    return JsonResponse(data)