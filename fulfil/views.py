from django.shortcuts import render
from .models import EnrollCourse, Main, WhoForCourse, WhyShouldStudyCourse, WhyShouldStudyProfession
from .forms import EnrollCourseForm


def home(request):
    main = Main.objects.get()
    who_for_courses = WhoForCourse.objects.all()
    why_should_study_courses = WhyShouldStudyCourse.objects.all()
    text_split = main.course_body.split("?")
    teacher_about = main.teacher_about.split(".")
    why_projects = main.course_project_content.split(".")

    # Nega sun'iy intellektni o'rganishim kerak?
    why_profession_courses = WhyShouldStudyProfession.objects.all()[:2]
    why_profession_courses1 = WhyShouldStudyProfession.objects.all()[2:]

    # print(teacher_about)
    # print(text_split)
    # print(why_projects)

    if request.method == 'POST':
        model = EnrollCourse()
        model.full_name = request.POST.get('firstname', '')
        model.phone_number = request.POST.get('lastname', '')
        model.tg_username = request.POST.get('username', '')

        if form.is_valid():
            model.save()

    context = {
        'main': main,
        'text_split': text_split,
        'teacher_about': teacher_about,
        'who_for_courses': who_for_courses,
        'why_projects': why_projects,
        'why_should_study_courses': why_should_study_courses,
        'why_profession_courses': why_profession_courses,
        'why_profession_courses1': why_profession_courses1,
    }

    return render(request, 'index.html', context)
