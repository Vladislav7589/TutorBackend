from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import PasswordField

from .models import Student, Tutor, Subject, Lesson, TutorSubject, Record, Payment, CustomUser, \
    StudentRequest

from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
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
