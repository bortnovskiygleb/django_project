from django.shortcuts import render
import components


def weather(request):
    list_weather = components.select_current_weather()
    three_hours_weather = list_weather[:3]
    if request.method == "POST":
        if 'city' in request.POST:
            city = request.POST['city']
            city_weather = components.get_weather_by_city(city)
        if 'date' in request.POST:
            date = request.POST['date'].split('-')
            weather_date = components.select_weather_by_date(date[0], date[1], date[2])
            if weather_date == -1:
                error = 'Неправильный формат ввода'
                weather_date = {'day_temperature': '', 'night_temperature': ''}
            else:
                weather_date_day = weather_date['day_temperature']
                weather_date_night = weather_date['night_temperature']
    return render(request, 'weather.html', locals())


