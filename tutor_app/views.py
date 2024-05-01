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
    TutorSubjectSerializer, RecordSerializer, StudentRequestSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

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
    filterset_fields = ['id', 'city']
    filter_backends = [SearchFilter]
    #permission_classes = [IsAuthenticated]
    #search_fields = ['first_name', 'last_name']

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
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def email_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    # Пытаемся получить пользователя по адресу электронной почты
    try:
        user = CustomUser.objects.get(password=password)
    except CustomUser.DoesNotExist:
        user = None
    user_data = serializers.serialize('json', [user])
    print(user.check_password(password))

    if user is not None and user.check_password(password):
        # Пользователь успешно аутентифицирован
        # Возвращаем токены доступа и обновления
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        # Пользователь не найден или неверный пароль
        return Response({'error': f'Invalid credentials   ${user_data}'}, status=status.HTTP_401_UNAUTHORIZED)