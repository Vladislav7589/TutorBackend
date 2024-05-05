from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с указанным email и паролем.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password"]
    email = models.EmailField(unique=True, null=False)
    middle_name = models.CharField(blank=True, max_length=150)
    username = None
    city = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=20, null=True)
    user_type = models.CharField(max_length=100, )  # Student/Tutor


class Tutor(models.Model):
    tutor_id = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=100)
    brief_info = models.CharField(max_length=255)
    educational_institution = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tutor_id}'


class Student(models.Model):
    student_id = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.student_id}'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'Tutor':
            Tutor.objects.create(tutor_id=instance)
        elif instance.user_type == 'Student':
            Student.objects.create(student_id=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 'Tutor':
        instance.tutor.save()
    elif instance.user_type == 'Student':
        instance.student.save()


# @receiver(pre_delete, sender=Tutor)
# def delete_related_user(sender, instance, **kwargs):
#     if instance.tutor_id:
#         instance.tutor_id.delete()


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.subject_id}: {self.name}'


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


class StudentRequest(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Record(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Payment(models.Model):
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=100)


class Review(models.Model):
    tutor_id = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    rating = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f'Оценка о {self.tutor} от {self.student}'

