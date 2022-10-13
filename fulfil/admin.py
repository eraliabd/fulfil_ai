from django.contrib import admin
from .models import EnrollCourse, Main, WhoForCourse, WhyShouldStudyCourse, WhyShouldStudyProfession, \
    CommentAboutCourse, WhatThisLearnCourse

admin.site.register(EnrollCourse)
admin.site.register(Main)
admin.site.register(WhoForCourse)
admin.site.register(WhyShouldStudyCourse)
admin.site.register(WhyShouldStudyProfession)
admin.site.register(CommentAboutCourse)
admin.site.register(WhatThisLearnCourse)
