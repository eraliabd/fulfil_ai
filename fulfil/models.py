from django.db import models


# enroll course model
class EnrollCourse(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    tg_username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
