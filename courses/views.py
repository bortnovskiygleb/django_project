from django.shortcuts import render
import components
from .forms import CourseDateForm


def courses(request):
    list_courses = components.select_current_courses()
    form = CourseDateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        date = str(form.cleaned_data['date']).split('-')
        courses_date = components.select_courses_by_date(date[0], date[1], date[2])
        if courses_date == -1:
            error = 'Неправильный формат ввода'
            courses_date = []

    return render(request, 'courses.html', locals())
