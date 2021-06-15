from django.shortcuts import render
from django.views import View

from .models import Level

import random


class LevelView(View):
    """Список рівнів складності"""
    def get(self, request):
        levels = Level.objects.all()
        return render(request, 'punishments/level_list.html', {'level_list': levels})


class LevelDetailView(View):
    """Всі завдання на даному рівні складності"""
    def get(self, request, slug):
        level = Level.objects.get(url=slug)
        punishments = level.punishment_set.all()
        punishment = random.choice(punishments)
        return render(request, 'punishments/level_detail.html', {'level': level, 'punishment': punishment,})
