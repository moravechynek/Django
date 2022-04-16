from django.forms import ModelForm

from .models import Otazka, Odpoved

class OdpovedForm(ModelForm):

    class Meta:
        model = Odpoved
        fields = '__all__'