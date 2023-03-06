# 4. Life in weeks calculator basing on that you will live 90 years:

print("Life in weeks calculator basing on that you will live 90 years")
age = input("What is your current age? ")
age_num = int(age)
year1_days = (90 * 365) - (365 * age_num)
year1_weeks = (90 * 52) - (52 * age_num)
year1_months = (90 * 12) - (12 * age_num)
print(f"You have {year1_days} days, {year1_weeks} weeks, {year1_months} months l


# 4. another way:

print("Life in weeks calculator basing on that you will live 90 years")
age = input("What is your current age? ")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = 365 * years_remaining
weeks_remaining = 52 * years_remaining
months_remaining = 12 * years_remaining
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"
print(message)
