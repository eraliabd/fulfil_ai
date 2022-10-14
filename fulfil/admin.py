from django.contrib import admin
from .models import EnrollCourse, Main, WhoForCourse, WhyShouldStudyCourse, WhyShouldStudyProfession, \
    CommentAboutCourse, WhatThisLearnCourse


class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'tg_username', 'created_at')
    list_display_links = ('id', 'full_name',)
    list_filter = ('created_at',)
    search_fields = ('full_name', 'phone_number', 'tg_username',)


class MainAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_title', 'full_name')
    list_display_links = ('id', 'course_title')
    search_fields = ('course_title', 'full_name')


class CommentAboutCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'definition')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', 'definition')


admin.site.register(EnrollCourse, EnrollCourseAdmin)
admin.site.register(Main, MainAdmin)
admin.site.register(WhoForCourse)
admin.site.register(WhyShouldStudyCourse)
admin.site.register(WhyShouldStudyProfession)
admin.site.register(CommentAboutCourse, CommentAboutCourseAdmin)
admin.site.register(WhatThisLearnCourse)
