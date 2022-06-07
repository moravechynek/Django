from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Otazka, Odpoved


class OdpovedForm(forms.ModelForm):

    def __init__(self, *args, otazka, **kwargs):
        super(OdpovedForm, self).__init__(*args, **kwargs)
        if otazka.odpoved_c:
            answer_choices = [('a', 'A. ' + otazka.odpoved_a), ('b', 'B. ' + otazka.odpoved_b), ('c', 'C. ' + otazka.odpoved_c)]
        else:
            answer_choices = [('a', 'A. ' + otazka.odpoved_a), ('b', 'B. ' + otazka.odpoved_b)]
        self.fields["odpoved"] = forms.ChoiceField(
            widget=forms.RadioSelect(),
            choices=answer_choices
        )


    class Meta:
        model = Odpoved
        fields = ('odpoved',)

