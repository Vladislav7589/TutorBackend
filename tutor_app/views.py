from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student, Tutor, Subject, Lesson, TutorSubject, StudentRequest, Record, Payment
from tutor_app.models import CustomUser
from .serializers import SubjectSerializer, StudentSerializer, TutorSerializer, UsersSerializer, LessonSerializer, \
    TutorSubjectSerializer, RecordSerializer, StudentRequestSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, world")

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id']
    filter_backends = [SearchFilter]
    #permission_classes = [IsAuthenticated]
    #search_fields = ['first_name', 'last_name']


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
class TutorSubjectViewSet(ModelViewSet):
    queryset = TutorSubject.objects.all()
    serializer_class = TutorSubjectSerializer
    filterset_fields = ['tutor_id']
    filter_backends = [SearchFilter]
    search_fields = []

class StudentRequestViewSet(ModelViewSet):
    queryset = StudentRequest.objects.all()
    serializer_class = StudentRequestSerializer
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


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        user_id = user_data['id']
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': user_id,  # Добавляем данные о пользователе
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def email_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)

    except CustomUser.DoesNotExist:
        user = None

    if user is not None and user.check_password(password):

        refresh = RefreshToken.for_user(user)

        user_data = UserSerializer(user).data
        user_id = user_data['id']
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': user_id,
        })
    else:
        # Пользователь не найден или неверный пароль
        return Response({'error': f'Invalid credentials '}, status=status.HTTP_401_UNAUTHORIZED)

