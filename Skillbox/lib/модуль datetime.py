# import time
#
# print(time.gmtime(0))  # проверка начала эпохи на машине
# print(time.time())  # прошло секунд с начала эпохи
# print(time.sleep(2))  # заснуть на две секунды
#
# start = time.monotonic()  # всегда движется вперед
# long_num = 2 ** 10 ** 8
# dur = time.monotonic() - start
# print(f"Время вычеслений составило {dur} секунд")


import datetime


my_date = datetime.date(year=1994, month=11, day=30)
print(f"Мой день рождения {my_date}")
print(f"Я родился в {my_date.year} году. Это был {my_date.month} месяц. {my_date.day} числа")
print(f"Это был день недели {my_date.weekday()}")

my_time = datetime.time(hour=2, minute=14, second=54, microsecond=4342)
print(f"Мой время {my_time}")

print(f"Мой день рождения, красивый формат {my_date.strftime('%d.%m.%Y')}")

d1 = "01.02.2022"
d1_date = datetime.datetime.strptime(d1, '%d.%m.%Y')
print(d1_date)
new_my_day = datetime.datetime.combine(my_date, my_time)
print(f"Мой дата время: {new_my_day}")

t_delt = d1_date - new_my_day
print(t_delt)

now = datetime.datetime.now().date()
print("Прошло дней с момента рождения", now - my_date )

# для работы с таймзонами библиотека pytz
import pytz
print("Все временные зоны:", pytz.all_timezones)


import calendar
my_cal = calendar.TextCalendar(firstweekday=0)
print(my_cal.formatmonth(2022, 9))
my_cal = calendar.HTMLCalendar(firstweekday=0)
print(my_cal.formatmonth(2022, 9))


