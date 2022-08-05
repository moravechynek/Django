# Generated by Django 3.1.7 on 2022-08-05 06:57

import autoskola.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Odstavec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraf', models.CharField(max_length=5)),
                ('odstavec', models.IntegerField()),
                ('obsah', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Odstavec',
                'verbose_name_plural': 'Odstavce',
            },
        ),
        migrations.CreateModel(
            name='Zakon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cislo', models.CharField(max_length=50)),
                ('nazev', models.TextField(max_length=300)),
                ('typ', models.CharField(choices=[('Z', 'Zákon'), ('V', 'Vyhláška')], default='Z', max_length=1)),
            ],
            options={
                'verbose_name': 'Zákon',
                'verbose_name_plural': 'Zákony',
            },
        ),
        migrations.CreateModel(
            name='Znacka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cislo', models.CharField(max_length=10)),
                ('obrazek', models.ImageField(upload_to=autoskola.models.get_image_znacky)),
                ('nazev', models.CharField(max_length=95)),
                ('vyznam', models.TextField(max_length=925)),
                ('typ', models.CharField(choices=[('A', 'Výstražné'), ('P', 'Upravující přednost'), ('B', 'Zákazové'), ('C', 'Příkazové'), ('IZ', 'Informativní zónové'), ('IP', 'Informativní provozní'), ('IS', 'Informativní směrové'), ('IJ', 'Informativní jiné'), ('E', 'Dodatkové tabulky'), ('1', 'Kulturní a turistické piktogramy'), ('2', 'Druhy vozidel a skupiny chodců'), ('3', 'Jiné a cíle'), ('4', 'Ostatní symboly'), ('V', 'Vodorovné dopravní značky'), ('S', 'Světelné signály'), ('Z', 'Dopravní zařízení'), ('ZPI', 'Dopravní zařízení'), ('O', 'Speciální označení vozidel a parkovací průkaz označující vozidlo přepravující osobu těžce zdravotně postiženou')], default='A', max_length=3)),
            ],
            options={
                'verbose_name': 'Značka',
                'verbose_name_plural': 'Značky',
            },
        ),
        migrations.CreateModel(
            name='Otazka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otazka', models.TextField(max_length=150)),
                ('obrazek', models.ImageField(blank=True, upload_to=autoskola.models.get_image_otazky)),
                ('file', models.FileField(blank=True, upload_to=autoskola.models.get_image_otazky)),
                ('odpoved_a', models.TextField(max_length=300)),
                ('odpoved_b', models.TextField(max_length=300)),
                ('odpoved_c', models.TextField(max_length=300)),
                ('spravna_odpoved', models.CharField(max_length=1)),
                ('FK_odstavec', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoskola.odstavec')),
                ('FK_znacka', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autoskola.znacka')),
            ],
            options={
                'verbose_name': 'Otázka',
                'verbose_name_plural': 'Otázky',
            },
        ),
        migrations.AddField(
            model_name='odstavec',
            name='FK_zakon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autoskola.zakon'),
        ),
        migrations.CreateModel(
            name='Odpoved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odpoved', models.TextField(max_length=150)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('FK_otazka', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='autoskola.otazka')),
            ],
            options={
                'verbose_name': 'Odpověď',
                'verbose_name_plural': 'Odpovědi',
            },
        ),
    ]
