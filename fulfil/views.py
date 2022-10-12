from django.shortcuts import render
from .models import EnrollCourse
from .forms import EnrollCourseForm


def home(request):
    form = EnrollCourseForm()
    if request.method == 'POST':
        model = EnrollCourse()
        model.full_name = request.POST.get('firstname', '')
        model.phone_number = request.POST.get('lastname', '')
        model.tg_username = request.POST.get('username', '')

        if form.is_valid():
            model.save()

    context = {
        '',
    }

    return render(request, 'index.html', context=None)
