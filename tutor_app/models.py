from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import filters


class CustomUser(AbstractUser):
    city = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=20)
    user_type = models.CharField(max_length=100)  # Student/Tutor
    active_account = models.BooleanField(null=True)


class Tutor(models.Model):
    tutor_id = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=100)
    brief_info = models.CharField(max_length=255)
    educational_institution = models.CharField(max_length=100)


class Student(models.Model):
    student_id = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=100)


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Id: {self.subject_id} name: {self.name}'


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=100)


class TutorSubject(models.Model):
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)


class TutorRequest(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Record(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=100)

# Create your models here.