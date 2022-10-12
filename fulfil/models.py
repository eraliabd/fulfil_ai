from django.db import models


# enroll course model
class EnrollCourse(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.PositiveBigIntegerField()
    tg_username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Main(models.Model):
    # navbar qismidagi telefon raqam
    phone_number = models.CharField(max_length=20, null=True)
    # ASOSIY RASMLAR, KETMA-KET JOYLASHGAN
    # 240 soatlik professional Python va Sun’iy intellekt kursi
    course_image = models.ImageField(upload_to='course_image/', null=True)
    course_title = models.CharField(max_length=255, null=True)
    course_body = models.TextField(null=True)
    # Biyimbetov Azizbek haqida va ustozni rasmi
    teacher_image = models.ImageField(upload_to='teacher_image/', null=True)
    full_name = models.CharField(max_length=255, null=True)
    teacher_about = models.TextField(null=True)
    # BU KURSDA NIMALARNI O'RGANAMIZ?
    course_learn_image = models.ImageField(upload_to='course_learn/', null=True)
    # Kursda qanday loyihalarni bajaramiz?
    course_project_image = models.ImageField(upload_to='course_project/', null=True)
    course_project_content = models.TextField(null=True)
    # YANA BIR IMKONIYAT
    course_chance_image = models.ImageField(upload_to='course_chance/', null=True)
    course_chance_content = models.TextField(null=True)
    # KURS VA USTOZ HAQIDA XULOSA CHIQARMOQCHIMISIZ?
    course_teacher_about_image = models.ImageField(upload_to='course_teacher_about/', null=True)

    # 20 Darslar
    lessons = models.IntegerField(null=True)

    # 30 dan ortiq vazifalar
    task = models.IntegerField(null=True)

    # Nega sun'iy intellektni o'rganishim kerak?
    why_should_study_profession_title = models.CharField(max_length=255, null=True)



# KURS KIMLAR UCHUN? Model
class WhoForCourse(models.Model):
    image = models.ImageField(upload_to='who_for_course/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# Nega sun'iy intellektni o'rganishim kerak?
class WhyShouldStudyProfession(models.Model):
    image = models.ImageField(upload_to='why_should_study_profession/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# Nega aynan bu kursda o’qishim kerak?
class WhyShouldStudyCourse(models.Model):
    image = models.ImageField(upload_to='why_should_study_course/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
