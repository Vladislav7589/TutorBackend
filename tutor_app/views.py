from django.http import HttpResponse
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Student, Tutor, Subject, Lesson, TutorSubject, TutorRequest, Record, Payment
from tutor_app.models import CustomUser
from .serializers import SubjectSerializer, StudentSerializer, TutorSerializer, UsersSerializer, LessonSerializer, \
    TutorSubjectSerializer, TutorRequestSerializer, RecordSerializer


def index(request):
    return HttpResponse("Hello, world")


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['student_id']
    filter_backends = [SearchFilter]
    search_fields = ['education_level']

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_fields = ['name', 'subject_id']
    filter_backends = [SearchFilter]
    search_fields = ['name', 'subject_id']

class TutorViewSet(ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    filterset_fields = ['tutor_id']
    filter_backends = [SearchFilter]
    search_fields = ['educational_institution']

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filterset_fields = ['lesson_id', 'date']
    filter_backends = [SearchFilter]
    search_fields = ['date']

class UsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['id', 'subject_id', 'city']
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']

class TutorSubjectViewSet(ModelViewSet):
    queryset = TutorSubject.objects.all()
    serializer_class = TutorSubjectSerializer
    filterset_fields = ['tutor_id']
    filter_backends = [SearchFilter]
    search_fields = []

class TutorRequestViewSet(ModelViewSet):
    queryset = TutorRequest.objects.all()
    serializer_class = TutorRequestSerializer
    filterset_fields = ['student_id']
    filter_backends = [SearchFilter]
    search_fields = []

class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filterset_fields = ['lesson_id', 'student_id']
    filter_backends = [SearchFilter]
    search_fields = []

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = RecordSerializer
    filterset_fields = ['payment_id', 'lesson_id']
    filter_backends = [SearchFilter]
    search_fields = []

