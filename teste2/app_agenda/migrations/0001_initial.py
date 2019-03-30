# Generated by Django 2.1.7 on 2019-03-29 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento:')),
                ('titulo', models.CharField(max_length=128, verbose_name='Título')),
                ('nota', models.TextField(blank=True, null=True, verbose_name='Nota')),
                ('privado', models.BooleanField(blank=True, null=True, verbose_name='Privado?')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
    ]