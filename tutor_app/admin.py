from django.contrib import admin
from .models import Student, Tutor, Subject, Lesson, TutorSubject, TutorRequest, Record, Payment
from tutor_app.models import CustomUser

admin.site.register(CustomUser)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(TutorSubject)
admin.site.register(TutorRequest)
admin.site.register(Record)
admin.site.register(Payment)

# Register your models here.
