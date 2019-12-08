from django.shortcuts import render
import components
from . forms import MovieDateForm


def movies(request):
    list_movies = components.select_current_movies()
    form = MovieDateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        date = str(form.cleaned_data['date']).split('-')
        movies_date = components.select_movies_by_date(date[0], date[1], date[2])
        if movies_date == -1:
            error = 'Неправильный формат ввода'
            movies_date = []
        elif not movies_date:
            error = 'В этот день премьер не было'
            movies_date = []
    return render(request, 'movies.html', locals())

