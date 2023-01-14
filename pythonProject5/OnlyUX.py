import csv

with open("vacancies_with_skills.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)

    with open("OnlyUX.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
        fields = [
            "name",
            "salary_from",
            "salary_to",
            "salary_currency",
            "area_name",
            "published_at",
        ]
        writer = csv.writer(csvfile, dialect=csv.unix_dialect)
        writer.writerow(fields)
        for row in reader:
            if (
                "UX/UI дизайнер" in str(row["name"])
                or "design" in str(row["name"])
                or " ux " in str(row["name"])
                or " ui " in str(row["name"])
                or "дизайн" in str(row["name"])
                or "иллюстратор" in str(row["name"])
            ):
                writer.writerow(
                    [
                        row["name"],
                        row["salary_from"],
                        row["salary_to"],
                        row["salary_currency"],
                        row["area_name"],
                        row["published_at"],
                    ]
                )
