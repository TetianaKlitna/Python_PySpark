from datetime import date


def life_in_weeks(age):
    start_date = date.today()
    year = start_date.year
    end_date = date(year, 12, 31)
    extra_days = 0
    full_weeks = 0
    while age <= 90:
        diff_days = (end_date - start_date).days + extra_days
        full_weeks += diff_days//7
        extra_days = diff_days % 7
        age += 1
        year += 1
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
    print(f"You have {full_weeks} weeks until 90 years old")


life_in_weeks(20)
