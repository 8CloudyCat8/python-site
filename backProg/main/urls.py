from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("demand", views.demand, name="demand"),
    path("geography", views.geography, name="geography"),
    path("skills", views.skills, name="skills"),
    path("lastVacancies", views.lastVacancies, name="lastVacancies"),
]
