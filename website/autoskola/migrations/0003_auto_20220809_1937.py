# Generated by Django 3.1.7 on 2022-08-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoskola', '0002_remove_otazka_obrazek'),
    ]

    operations = [
        migrations.AddField(
            model_name='otazka',
            name='a_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='otazka',
            name='b_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='otazka',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
    ]
