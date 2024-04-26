from django.http import HttpResponse
from django.views.generic import ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Student, Tutor, Subject, Lesson, TutorSubject, TutorRequest, Record, Payment
from tutor_app.models import CustomUser
from .serializers import SubjectSerializer


def index(request):
    return HttpResponse("Hello, world")


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filterset_fields = ['name', 'subject_id']
    filter_backends = [SearchFilter]
    search_fields = ['name', 'subject_id']

