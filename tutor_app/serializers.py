from rest_framework.serializers import ModelSerializer
from .models import Student, Tutor, Subject, Lesson, TutorSubject, Record, Payment, CustomUser, \
    StudentRequest


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TutorSerializer(ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TutorSubjectSerializer(ModelSerializer):
    class Meta:
        model = TutorSubject
        fields = '__all__'


class StudentRequestSerializer(ModelSerializer):
    class Meta:
        model = StudentRequest
        fields = '__all__'


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class UsersSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
