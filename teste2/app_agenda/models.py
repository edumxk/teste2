from django.db import models

class Agenda(models.Model):
    
    data_evento = models.DateTimeField('Data do Evento:')
    titulo = models.CharField('Título', max_length=128)
    nota = models.TextField('Nota', blank = True, null = True)
    privado = models.BooleanField('Privado?', blank = True, null = True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
    def __str__(self):
        return self.titulo