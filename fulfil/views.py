from django.shortcuts import render, redirect
from django.db.models import F

from .forms import EnrollCourseForm
from .models import EnrollCourse, Main, WhoForCourse, WhyShouldStudyCourse, WhyShouldStudyProfession, \
    CommentAboutCourse, WhatThisLearnCourse


def home(request):
    # Bunda umumiy malumot keladi
    main = Main.objects.get()
    # KURS KIMLAR UCHUN?
    who_for_courses = WhoForCourse.objects.all()
    # Nega aynan bu kursda o’qishim kerak?
    why_should_study_courses = WhyShouldStudyCourse.objects.all()

    # BU KURSDA NIMALARNI O'RGANAMIZ?
    what_this_learn_courses_right = WhatThisLearnCourse.objects.annotate(odd=F('ordinal_number') % 2).filter(odd=False)
    what_this_learn_courses_left = WhatThisLearnCourse.objects.annotate(odd=F('ordinal_number') % 2).filter(odd=True)
    # print(what_this_learn_courses_right)
    # print(what_this_learn_courses_left)

    # 240 soatlik professional Python va Sun’iy intellekt kursi
    text_split = main.course_body.split("?")
    # Ustoz haqida
    teacher_about = main.teacher_about.split(".")
    # Kursda qanday loyihalarni bajaramiz?
    why_projects = main.course_project_content.split(".")

    # Nega sun'iy intellektni o'rganishim kerak?
    why_profession_courses = WhyShouldStudyProfession.objects.all()[:2]
    why_profession_courses1 = WhyShouldStudyProfession.objects.all()[2:]

    # Kursimiz haqida izohlar
    comment_first = CommentAboutCourse.objects.all()[:2]
    comment_second = CommentAboutCourse.objects.all()[2:]

    # print(teacher_about)
    # print(text_split)
    # print(why_projects)

    if request.method == 'POST':
        model = EnrollCourse()
        model.full_name = request.POST.get('firstname', '')
        model.phone_number = request.POST.get('lastname', '')
        model.tg_username = request.POST.get('username', '')

        model.save()

        # actions = request.session.get('actions', [])
        # actions += [f"{request.POST.get('firstname')}", f"{request.POST.get('lastname')}", f"{request.POST.get('username')}"]
        # request.session['actions'] = actions
        # print(actions)

    context = {
        'main': main,
        'text_split': text_split,
        'teacher_about': teacher_about,
        'who_for_courses': who_for_courses,
        'why_projects': why_projects,
        'why_should_study_courses': why_should_study_courses,
        'why_profession_courses': why_profession_courses,
        'why_profession_courses1': why_profession_courses1,
        'what_this_learn_courses_left': what_this_learn_courses_left,
        'what_this_learn_courses_right': what_this_learn_courses_right,
        'comment_first': comment_first,
        'comment_second': comment_second,
    }

    return render(request, 'index.html', context)


def success(request):
    # Bunda umumiy malumot keladi
    main = Main.objects.get()
    # KURS KIMLAR UCHUN?
    who_for_courses = WhoForCourse.objects.all()
    # Nega aynan bu kursda o’qishim kerak?
    why_should_study_courses = WhyShouldStudyCourse.objects.all()

    # BU KURSDA NIMALARNI O'RGANAMIZ?
    what_this_learn_courses_right = WhatThisLearnCourse.objects.annotate(odd=F('ordinal_number') % 2).filter(odd=False)
    what_this_learn_courses_left = WhatThisLearnCourse.objects.annotate(odd=F('ordinal_number') % 2).filter(odd=True)
    # print(what_this_learn_courses_right)
    # print(what_this_learn_courses_left)

    # 240 soatlik professional Python va Sun’iy intellekt kursi
    text_split = main.course_body.split("?")
    # Ustoz haqida
    teacher_about = main.teacher_about.split(".")
    # Kursda qanday loyihalarni bajaramiz?
    why_projects = main.course_project_content.split(".")

    # Nega sun'iy intellektni o'rganishim kerak?
    why_profession_courses = WhyShouldStudyProfession.objects.all()[:2]
    why_profession_courses1 = WhyShouldStudyProfession.objects.all()[2:]

    # Kursimiz haqida izohlar
    comment_first = CommentAboutCourse.objects.all()[:2]
    comment_second = CommentAboutCourse.objects.all()[2:]

    # print(teacher_about)
    # print(text_split)
    # print(why_projects)

    if request.method == 'POST':
        model = EnrollCourse()
        model.full_name = request.POST.get('firstname', '')
        model.phone_number = request.POST.get('lastname', '')
        model.tg_username = request.POST.get('username', '')

        model.save()

        # actions = request.session.get('actions', [])
        # actions += [f"{request.POST.get('firstname')}", f"{request.POST.get('lastname')}", f"{request.POST.get('username')}"]
        # request.session['actions'] = actions
        # print(actions)

    context = {
        'main': main,
        'text_split': text_split,
        'teacher_about': teacher_about,
        'who_for_courses': who_for_courses,
        'why_projects': why_projects,
        'why_should_study_courses': why_should_study_courses,
        'why_profession_courses': why_profession_courses,
        'why_profession_courses1': why_profession_courses1,
        'what_this_learn_courses_left': what_this_learn_courses_left,
        'what_this_learn_courses_right': what_this_learn_courses_right,
        'comment_first': comment_first,
        'comment_second': comment_second,
    }

    return render(request, 'index.html', context)
