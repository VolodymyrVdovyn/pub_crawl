from django.db import models
from django.shortcuts import reverse


class Level(models.Model):
    """Рівень складності покарання"""
    name = models.CharField('Назва', max_length=100, unique=True)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рівень складності'
        verbose_name_plural = 'Рівні складності'


class Punishment(models.Model):
    """Покарання"""
    name = models.CharField('Назва', max_length=100, unique=True)
    description = models.TextField('Опис')
    # url = models.SlugField(max_length=130, unique=True, null=True)

    level = models.ForeignKey(
        Level, verbose_name='Рівень складності', on_delete=models.PROTECT, null=True) # related_name='punishment',

    # draft = models.BooleanField('Чернетка', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Покарання'
        verbose_name_plural = 'Покарання'
