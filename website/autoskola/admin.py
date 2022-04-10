from django.contrib import admin

from .models import Zakon, Znacka, Otazka, Odstavec, Odpoved

admin.site.register(Zakon)
admin.site.register(Znacka)
admin.site.register(Otazka)
admin.site.register(Odstavec)
admin.site.register(Odpoved)
