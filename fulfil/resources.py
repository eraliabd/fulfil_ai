from import_export import resources
from .models import EnrollCourse


class EnrollCourseResource(resources.ModelResource):
    class Meta:
        model = EnrollCourse
