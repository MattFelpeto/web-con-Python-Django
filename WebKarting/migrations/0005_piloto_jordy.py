# Generated by Django 4.2.6 on 2023-11-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebKarting', '0004_piloto_fernando'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piloto_Jordy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.CharField(max_length=60, verbose_name='Puntaje actual')),
                ('carreras_ganadas', models.CharField(max_length=60, verbose_name='Carreras Ganadas')),
                ('fechas_completadas', models.CharField(max_length=60, verbose_name='Fechas Completadas')),
            ],
        ),
    ]
