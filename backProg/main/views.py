from django.shortcuts import render
from .models import *


def main(request):
    stats = Stats.objects
    firstPhoto = stats.filter(id=1)
    secondPhoto = stats.filter(id=2)
    thirdPhoto = stats.filter(id=3)
    fourthPhoto = stats.filter(id=4)
    return render(
        request,
        "main/index.html",
        {
            "title": "Ux/Ui-designer",
            "firstPhoto": firstPhoto,
            "secondPhoto": secondPhoto,
            "thirdPhoto": thirdPhoto,
            "fourthPhoto": fourthPhoto,
        },
    )


def demand(request):
    images = Demand.objects.all()

    return render(
        request, "main/demand.html", {"title": "Востребованность", "photos": images}
    )


def geography(request):
    images = Geography.objects.all()
    return render(
        request, "main/geography.html", {"title": "География", "photos": images}
    )


def skills(request):
    images = Skills.objects.all()
    return render(request, "main/skills.html", {"title": "Навыки", "photos": images})


def lastVacancies(request):
    return render(request, "main/lastVacancies.html")
