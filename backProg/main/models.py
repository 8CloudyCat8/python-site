from django.db import models
from django.urls import reverse


class Stats(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"


class Demand(models.Model):
    tableImg = models.ImageField(upload_to="demand/")
    graphImg = models.ImageField(upload_to="demand/")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Востребованность"
        verbose_name_plural = "Востребованность"


class Geography(models.Model):
    tableImg = models.ImageField(upload_to="geography/")
    graphImg = models.ImageField(upload_to="geography/")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "География"
        verbose_name_plural = "География"


class Skills(models.Model):
    tableImg = models.ImageField(upload_to="skills/")
    graphImg = models.ImageField(upload_to="skills/")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"


class Vacancies(models.Model):
    tableImg = models.ImageField(upload_to="Vacancies/")
    graphImg = models.ImageField(upload_to="Vacancies/")

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})

    class Meta:
        verbose_name = "Последние вакансии"
        verbose_name_plural = "Последние вакансии"
