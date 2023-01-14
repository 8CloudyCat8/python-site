import csv

currency_to_rub = {
    "AZN": 35.68,
    "BYR": 23.91,
    "EUR": 59.90,
    "GEL": 21.74,
    "KGS": 0.76,
    "KZT": 0.13,
    "RUR": 1,
    "UAH": 1.64,
    "USD": 60.66,
    "UZS": 0.0055,
}


with open("OnlyUX.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    year_2010 = []
    salary2010 = 0
    year_2011 = []
    salary2011 = 0
    year_2012 = []
    salary2012 = 0
    year_2013 = []
    salary2013 = 0
    year_2014 = []
    salary2014 = 0
    year_2015 = []
    salary2015 = 0
    year_2016 = []
    salary2016 = 0
    year_2017 = []
    salary2017 = 0
    year_2018 = []
    salary2018 = 0
    year_2019 = []
    salary2019 = 0
    year_2020 = []
    salary2020 = 0
    year_2021 = []
    salary2021 = 0
    year_2022 = []
    salary2022 = 0

    for row in reader:

        down = 0
        up = 0

        if len(row["salary_from"]) != 0:
            down = float(row["salary_from"])

        if len(row["salary_to"]) != 0:
            up = float(row["salary_to"])
        salary = (float(up) + float(down)) // 2

        if str(row["salary_currency"]) != "RUR":
            if str(row["salary_currency"]) != "":
                if len(row["salary_from"]) != 0:
                    down = float(currency_to_rub[str(row["salary_currency"])]) * float(
                        row["salary_from"]
                    )
                if len(row["salary_to"]) != 0:
                    up = float(currency_to_rub[str(row["salary_currency"])]) * float(
                        row["salary_to"]
                    )
        if down > 0 and up > 0:
            salary = (float(up) + float(down)) // 2
        elif down == 0 and up != 0:
            salary = float(down)
        elif down != 0 and up == 0:
            salary = float(down)
        if salary != 0:
            if str(row["published_at"][:4]) == "2010":
                year_2010.append(row)
                salary2010 += salary
            if str(row["published_at"][:4]) == "2011":
                year_2011.append(row)
                salary2011 += salary
            if str(row["published_at"][:4]) == "2012":
                year_2012.append(row)
                salary2012 += salary
            if str(row["published_at"][:4]) == "2013":
                year_2013.append(row)
                salary2013 += salary

            if str(row["published_at"][:4]) == "2014":
                year_2014.append(row)
                salary2014 += salary
            if str(row["published_at"][:4]) == "2015":
                year_2015.append(row)
                salary2015 += salary
            if str(row["published_at"][:4]) == "2016":
                year_2016.append(row)
                salary2016 += salary
            if str(row["published_at"][:4]) == "2017":
                year_2017.append(row)
                salary2017 += salary
            if str(row["published_at"][:4]) == "2018":
                year_2018.append(row)
                salary2018 += salary
            if str(row["published_at"][:4]) == "2019":
                year_2019.append(row)
                salary2019 += salary
            if str(row["published_at"][:4]) == "2020":
                year_2020.append(row)
                salary2020 += salary
            if str(row["published_at"][:4]) == "2021":
                year_2021.append(row)
                salary2021 += salary
            if str(row["published_at"][:4]) == "2022":
                year_2022.append(row)
                salary2022 += salary


with open("Count_Vacancies_UX.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    fields = ["Год", "Количество вакансий"]
    writer = csv.writer(csvfile, dialect=csv.unix_dialect)
    writer.writerow(fields)
    writer.writerow(["2010", len(year_2010)])
    writer.writerow(["2011", len(year_2011)])
    writer.writerow(["2012", len(year_2012)])
    writer.writerow(["2013", len(year_2013)])
    writer.writerow(["2014", len(year_2014)])
    writer.writerow(["2015", len(year_2015)])
    writer.writerow(["2016", len(year_2016)])
    writer.writerow(["2017", len(year_2017)])
    writer.writerow(["2018", len(year_2018)])
    writer.writerow(["2019", len(year_2019)])
    writer.writerow(["2020", len(year_2020)])
    writer.writerow(["2021", len(year_2021)])
    writer.writerow(["2022", len(year_2022)])

    writer.writerow(["", ""])

    fields2 = ["Год", "Зарплата"]
    writer.writerow(fields2)
    writer.writerow(["2010", str(int(salary2010 / len(year_2010)))])
    writer.writerow(["2011", str(int(salary2011 / len(year_2011)))])
    writer.writerow(["2012", str(int(salary2012 / len(year_2012)))])
    writer.writerow(["2013", str(int(salary2013 / len(year_2013)))])
    writer.writerow(["2014", str(int(salary2014 / len(year_2014)))])
    writer.writerow(["2015", str(int(salary2015 / len(year_2015)))])
    writer.writerow(["2016", str(int(salary2016 / len(year_2016)))])
    writer.writerow(["2017", str(int(salary2017 / len(year_2017)))])
    writer.writerow(["2018", str(int(salary2018 / len(year_2018)))])
    writer.writerow(["2019", str(int(salary2019 / len(year_2019)))])
    writer.writerow(["2020", str(int(salary2020 / len(year_2020)))])
    writer.writerow(["2021", str(int(salary2021 / len(year_2021)))])
    writer.writerow(["2022", str(int(salary2022 / len(year_2022)))])
