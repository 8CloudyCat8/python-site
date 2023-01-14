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


with open("vacancies_dif_currencies.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)

    year2003 = [0]
    salary2003 = 0
    year2004 = [0]
    salary2004 = 0
    year2005 = []
    salary2005 = 0
    year2006 = []
    salary2006 = 0
    year2007 = []
    salary2007 = 0
    year2008 = []
    salary2008 = 0
    year2009 = []
    salary2009 = 0
    year2010 = []
    salary2010 = 0
    year2011 = []
    salary2011 = 0
    year2012 = []
    salary2012 = 0
    year2013 = []
    salary2013 = 0

    year2014 = []
    salary2014 = 0
    year2015 = []
    salary2015 = 0
    year2016 = []
    salary2016 = 0
    year2017 = []
    salary2017 = 0
    year2018 = []
    salary2018 = 0
    year2019 = []
    salary2019 = 0
    year2020 = []
    salary2020 = 0
    year2021 = []
    salary2021 = 0
    year2022 = []
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
        if down > 0:
            if up > 0:
                salary = (float(up) + float(down)) // 2
            elif down == 0 and up != 0:
                salary = float(down)
            elif down != 0 and up == 0:
                salary = float(down)
        elif down == 0 and up != 0:
            salary = float(down)
        elif down != 0 and up == 0:
            salary = float(down)
        if salary != 0:
            if str(row["published_at"][:4]) == "2003":
                year2003.append(row)
                salary2003 += salary
            if str(row["published_at"][:4]) == "2004":
                year2004.append(row)
                salary2004 += salary

            if str(row["published_at"][:4]) == "2005":
                year2005.append(row)
                salary2005 += salary

            if str(row["published_at"][:4]) == "2006":
                year2006.append(row)
                salary2006 += salary

            if str(row["published_at"][:4]) == "2007":
                year2007.append(row)
                salary2007 += salary
            if str(row["published_at"][:4]) == "2008":
                year2008.append(row)
                salary2008 += salary

            if str(row["published_at"][:4]) == "2009":
                year2009.append(row)
                salary2009 += salary

            if str(row["published_at"][:4]) == "2010":
                year2010.append(row)
                salary2010 += salary
            if str(row["published_at"][:4]) == "2011":
                year2011.append(row)
                salary2011 += salary
            if str(row["published_at"][:4]) == "2012":
                year2012.append(row)
                salary2012 += salary
            if str(row["published_at"][:4]) == "2013":
                year2013.append(row)
                salary2013 += salary
            if str(row["published_at"][:4]) == "2014":
                year2014.append(row)
                salary2014 += salary
            if str(row["published_at"][:4]) == "2015":
                year2015.append(row)
                salary2015 += salary
            if str(row["published_at"][:4]) == "2016":
                year2016.append(row)
                salary2016 += salary
            if str(row["published_at"][:4]) == "2017":
                year2017.append(row)
                salary2017 += salary
            if str(row["published_at"][:4]) == "2018":
                year2018.append(row)
                salary2018 += salary
            if str(row["published_at"][:4]) == "2019":
                year2019.append(row)
                salary2019 += salary
            if str(row["published_at"][:4]) == "2020":
                year2020.append(row)
                salary2020 += salary
            if str(row["published_at"][:4]) == "2021":
                year2021.append(row)
                salary2021 += salary
            if str(row["published_at"][:4]) == "2022":
                year2022.append(row)
                salary2022 += salary


with open("All.csv", "w", newline="", encoding="utf-8-sig") as csvfile:
    fields = ["Год", "Количество вакансий"]
    writer = csv.writer(csvfile, dialect=csv.unix_dialect)
    writer.writerow(fields)

    writer.writerow(["2003", len(year2003)])
    writer.writerow(["2004", len(year2004)])
    writer.writerow(["2005", len(year2005)])
    writer.writerow(["2006", len(year2006)])
    writer.writerow(["2007", len(year2007)])
    writer.writerow(["2008", len(year2008)])
    writer.writerow(["2009", len(year2009)])
    writer.writerow(["2010", len(year2010)])
    writer.writerow(["2011", len(year2011)])
    writer.writerow(["2012", len(year2012)])
    writer.writerow(["2013", len(year2013)])
    writer.writerow(["2014", len(year2014)])
    writer.writerow(["2015", len(year2015)])
    writer.writerow(["2016", len(year2016)])
    writer.writerow(["2017", len(year2017)])
    writer.writerow(["2018", len(year2018)])
    writer.writerow(["2019", len(year2019)])
    writer.writerow(["2020", len(year2020)])
    writer.writerow(["2021", len(year2021)])
    writer.writerow(["2022", len(year2022)])

    writer.writerow(["", ""])

    fields2 = ["Год", "Зарплата"]
    writer.writerow(fields2)
    writer.writerow(["2003", str(int(salary2003 / len(year2003)))])
    writer.writerow(["2004", str(int(salary2004 / len(year2004)))])
    writer.writerow(["2005", str(int(salary2005 / len(year2005)))])
    writer.writerow(["2006", str(int(salary2006 / len(year2006)))])
    writer.writerow(["2007", str(int(salary2007 / len(year2007)))])
    writer.writerow(["2008", str(int(salary2008 / len(year2008)))])
    writer.writerow(["2009", str(int(salary2009 / len(year2009)))])
    writer.writerow(["2010", str(int(salary2010 / len(year2010)))])
    writer.writerow(["2011", str(int(salary2011 / len(year2011)))])
    writer.writerow(["2012", str(int(salary2012 / len(year2012)))])
    writer.writerow(["2013", str(int(salary2013 / len(year2013)))])
    writer.writerow(["2014", str(int(salary2014 / len(year2014)))])
    writer.writerow(["2015", str(int(salary2015 / len(year2015)))])
    writer.writerow(["2016", str(int(salary2016 / len(year2016)))])
    writer.writerow(["2017", str(int(salary2017 / len(year2017)))])
    writer.writerow(["2018", str(int(salary2018 / len(year2018)))])
    writer.writerow(["2019", str(int(salary2019 / len(year2019)))])
    writer.writerow(["2020", str(int(salary2020 / len(year2020)))])
    writer.writerow(["2021", str(int(salary2021 / len(year2021)))])
    writer.writerow(["2022", str(int(salary2022 / len(year2022)))])
