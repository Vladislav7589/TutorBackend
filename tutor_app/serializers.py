from rest_framework.serializers import ModelSerializer
from .models import Student, Tutor, Subject, Lesson, TutorSubject, TutorRequest, Record, Payment
from tutor_app.models import CustomUser


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
