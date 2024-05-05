from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import PasswordField

from .models import Student, Tutor, Subject, Lesson, TutorSubject, Record, Payment, CustomUser, \
    StudentRequest, Review

from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
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


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


# class UsersSerializer(ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['student_id', 'date_and_time', 'rating', 'feedback']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class TutorWithReviewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Tutor
        fields = ['user', 'education_level', 'brief_info', 'educational_institution', 'reviews']


class CustomTutorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='tutor_id.email')
    middle_name = serializers.CharField(source='tutor_id.middle_name')
    first_name = serializers.CharField(source='tutor_id.first_name')
    last_name = serializers.CharField(source='tutor_id.last_name')
    city = serializers.CharField(source='tutor_id.city')
    date_of_birth = serializers.DateField(source='tutor_id.date_of_birth')
    phone = serializers.CharField(source='tutor_id.phone')

    subjects = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    def get_subjects(self, tutor_id):
        subjects = Subject.objects.filter(tutorsubject__tutor_id=tutor_id)
        return SubjectSerializer(subjects, many=True).data

    def get_reviews(self, tutor_id):
        reviews = Review.objects.filter(tutor_id_id=tutor_id)
        return ReviewSerializer(reviews, many=True).data
    class Meta:
        model = Tutor
        fields = ['tutor_id', 'education_level', 'brief_info', 'educational_institution', 'email', 'middle_name',
                  'first_name','last_name','city', 'date_of_birth', 'phone','subjects','reviews']
