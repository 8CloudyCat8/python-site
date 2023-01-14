from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Demand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tableImg", models.ImageField(upload_to="demand/")),
                ("graphImg", models.ImageField(upload_to="demand/")),
            ],
            options={
                "verbose_name": "Востребованность",
                "verbose_name_plural": "Востребованность",
            },
        ),
        migrations.CreateModel(
            name="Geography",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tableImg", models.ImageField(upload_to="geography/")),
                ("graphImg", models.ImageField(upload_to="geography/")),
            ],
            options={
                "verbose_name": "География",
                "verbose_name_plural": "География",
            },
        ),
        migrations.CreateModel(
            name="Skills",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tableImg", models.ImageField(upload_to="skills/")),
                ("graphImg", models.ImageField(upload_to="skills/")),
            ],
            options={
                "verbose_name": "Навыки",
                "verbose_name_plural": "Навык",
            },
        ),
        migrations.CreateModel(
            name="Vacancies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tableImg", models.ImageField(upload_to="Vacancies/")),
                ("graphImg", models.ImageField(upload_to="Vacancies/")),
            ],
            options={
                "verbose_name": "Последние вакансии",
                "verbose_name_plural": "Последние вакансию",
            },
        ),
        migrations.AlterModelOptions(
            name="stats",
            options={"verbose_name": "Статистика", "verbose_name_plural": "Статистика"},
        ),
    ]
