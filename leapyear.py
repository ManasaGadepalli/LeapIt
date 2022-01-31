# ask a user to enter their date of birth
import datetime
import calendar

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

birthday = input("Enter your birthday in MMDDYYYY format: ")

month = birthday[0:2]
converted_month = int(month)

day = birthday[2:4]
converted_day = int(day)

year = birthday[4:8]
converted_year = int(year)

week_day = calendar.weekday(converted_year, converted_month, converted_day)
print(f"You were born in {converted_year}, on a {weekdays[week_day]}")

year_list = []

if converted_year % 2 == 0 and converted_year % 4 != 0:
    constant = 11
elif converted_year % 4 == 0 and (converted_year + 1) % 2 != 0:
    constant = 6
else:
    constant = 5

for i in range(0, 3):
    actual_year = round(((5.6 * i) + converted_year + constant))
    year_list.append(actual_year)

for i in range(4, 6):
    actual_year = round(((6.88 * i) + converted_year + constant))
    year_list.append(actual_year)

for i in range(6, 8):
    actual_year = round(((6.5 * i) + converted_year + constant))
    year_list.append(actual_year)

for i in range(8, 10):
    actual_year = round(((6.94 * i) + converted_year + constant))
    year_list.append(actual_year)

print(year_list)
