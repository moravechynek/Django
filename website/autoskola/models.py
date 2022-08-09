import os
from django.db import models

def get_image_znacky(instance, filename):
    return os.path.join('autoskola/static/img/znacky', filename)

def get_image_otazky(instance, filename):
    return os.path.join('otazky', filename)

class Zakon(models.Model):
    cislo = models.CharField(max_length=50) # might be atomic
    nazev = models.TextField(max_length=300)

    ZAKON = 'Z'
    VYHLASKA = 'V'
    TYP = [
        (ZAKON, "Zákon"),
        (VYHLASKA, "Vyhláška"),
    ]
    typ = models.CharField(
        max_length=1,
        choices=TYP,
        default=ZAKON,
    )

    def __str__ (self):
        return (self.cislo + " " + self.nazev)

    class Meta:
        verbose_name = 'Zákon'
        verbose_name_plural = 'Zákony'

class Znacka(models.Model):
    cislo = models.CharField(max_length=10) # cely
    obrazek = models.ImageField(upload_to=get_image_znacky)
    nazev = models.CharField(max_length=95)
    vyznam = models.TextField(max_length=925)
    VYSTRAZNE = 'A'
    UPRAVUJICI_PREDNOST = 'P'
    ZAKAZOVE = 'B'
    PRIKAZOVE = 'C'
    INFORMATIVNI_ZONOVE = 'IZ'
    INFORMATIVNI_PROVOZNI = 'IP'
    INFORMATIVNI_SMEROVE = 'IS'
    INFORMATIVNI_JINE = 'IJ'
    DODATKOVE = 'E'
    KULTURNI_A_TURISTICKE = '1'
    DRUHY_VOZIDEL = '2'
    JINE_CILE = '3'
    OSTATNI_SYMBOLY = '4'
    VODOROVNE_PODELNE = 'V'
    SVETELNE = 'S'
    DOPRAVNI_ZARIZENI = 'Z'
    ZARIZENI_PRO_PROVOZNI_INFORMACE = 'ZPI'
    # VYSTRAZNE ODEVY
    SPECIALNI_OZNACENI = 'O'
    # POKYNY POLICISTU
    TYP = [
        (VYSTRAZNE, "Výstražné"),
        (UPRAVUJICI_PREDNOST, "Upravující přednost"),
        (ZAKAZOVE, "Zákazové"),
        (PRIKAZOVE, "Příkazové"),
        (INFORMATIVNI_ZONOVE, "Informativní zónové"),
        (INFORMATIVNI_PROVOZNI, "Informativní provozní"),
        (INFORMATIVNI_SMEROVE, "Informativní směrové"),
        (INFORMATIVNI_JINE, "Informativní jiné"),
        (DODATKOVE, "Dodatkové tabulky"),
        (KULTURNI_A_TURISTICKE, "Kulturní a turistické piktogramy"),
        (DRUHY_VOZIDEL, "Druhy vozidel a skupiny chodců"),
        (JINE_CILE, "Jiné a cíle"),
        (OSTATNI_SYMBOLY, "Ostatní symboly"),
        (VODOROVNE_PODELNE, "Vodorovné dopravní značky"),
        (SVETELNE, "Světelné signály"),
        (DOPRAVNI_ZARIZENI, "Dopravní zařízení"),
        # výstražné oděvy
        (ZARIZENI_PRO_PROVOZNI_INFORMACE, "Dopravní zařízení"),
        (SPECIALNI_OZNACENI, "Speciální označení vozidel a parkovací průkaz označující vozidlo přepravující osobu těžce zdravotně postiženou"),
        # pokyny policisty
    ]
    typ = models.CharField(
        max_length=3,
        choices=TYP,
        default=VYSTRAZNE,
    )
    def __str__ (self):
        return (self.cislo + " " + self.nazev)
    class Meta:
        verbose_name = 'Značka'
        verbose_name_plural = 'Značky'

class Otazka(models.Model):
    otazka = models.TextField(max_length=150)
    file = models.FileField(upload_to=get_image_otazky,
        blank=True)
    odpoved_a = models.TextField(max_length=300)
    a_id = models.IntegerField(default=0)
    odpoved_b = models.TextField(max_length=300)
    b_id = models.IntegerField(default=0)
    odpoved_c = models.TextField(max_length=300)
    c_id = models.IntegerField(default=0)
    spravna_odpoved = models.CharField(max_length=1)
    FK_odstavec = models.ForeignKey(
        'Odstavec',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    FK_znacka = models.ForeignKey(
        'Znacka',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__ (self):
        return (str(self.id) + ") " + self.otazka)

    class Meta:
        verbose_name = 'Otázka'
        verbose_name_plural = 'Otázky'

class Odstavec(models.Model):
    FK_zakon = models.ForeignKey(
        'Zakon',
        on_delete=models.CASCADE,
        default= 1,
        )
    paragraf = models.CharField(max_length=5) # bez §
    odstavec = models.IntegerField()
    obsah = models.TextField(max_length=500)
    class Meta:
        verbose_name = 'Odstavec'
        verbose_name_plural = 'Odstavce'

class Odpoved(models.Model):
    FK_otazka = models.ForeignKey(
        'Otazka',
        on_delete=models.CASCADE,
        default= 1,
    )
    odpoved = models.TextField(max_length=150)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.FK_otazka).split(')')[0] + ') ' + self.odpoved + ' ' + str(self.timestamp)

    class Meta:
        verbose_name = 'Odpověď'
        verbose_name_plural = 'Odpovědi'
