from django import forms
from .models import EnrollCourse


class EnrollCourseForm(forms.ModelForm):
    class Meta:
        model = EnrollCourse
        fields = ('full_name', 'phone_number', 'tg_username')
