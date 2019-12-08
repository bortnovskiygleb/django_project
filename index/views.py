from django.shortcuts import render
import datetime
from components import *


def index(request):
    up_date = select_date()
    hours = select_time().total_seconds() // 3600
    if datetime.datetime.today().month - up_date.month == 1 or datetime.datetime.today().month - up_date.month == -11:
        new_date = datetime.datetime.today()
        update_movies_in_database(new_date)
        update_weather_in_database(new_date)
        update_courses_in_database(new_date)
        update_information_date(new_date.year, new_date.month, new_date.day)
    if abs(datetime.datetime.now().hour - hours) > 0:
        insert_current_weather_in_database()
        insert_current_courses_in_database()
        insert_current_movies_in_database()
        new_time = datetime.datetime.now()
        update_information_time(new_time.hour, new_time.minute, new_time.second)
    return render(request, 'index.html', locals())

