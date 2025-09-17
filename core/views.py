from rest_framework.views import APIView
from core.models import University, College, Department, Course, Subject, Staff, Student
from core.serializers import (UniversitySerializer,CollegeSerializer,DepartmentSerializer,CourseSerializer,SubjectSerializer,StaffSerializer,StudentSerializer)
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .filters import UniversityFilter,CollegeFilter,DepartmentFilter,CourseFilter,SubjectFilter,StaffFilter,StudentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .paginations import CustomCursorPagination

class UniversityViewSet(viewsets.ModelViewSet):
    queryset=University.objects.all()
    serializer_class=UniversitySerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class = UniversityFilter
    search_fields=['name','location',]
    ordering_fields=['id','name','location','establishedYear']
    ordering=['name']
    pagination_class = CustomCursorPagination

class CollegeViewSet(viewsets.ModelViewSet):
    queryset=College.objects.all()
    serializer_class=CollegeSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class=CollegeFilter   
    search_fields=['name','location','universityId__name','universityId__location']
    ordering_fields=['id','name','location','universityId__name','universityId__location']
    ordering=['name']
    pagination_class=CustomCursorPagination

class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class=DepartmentSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class=DepartmentFilter
    search_fields=['name','hod','collegeId__name','collegeId__location','collegeId__universityId__name']
    ordering_fields=['id','name','hod','collegeId__name','collegeId__location','collegeId__universityId__name']
    ordering=['name']
    pagination_class=CustomCursorPagination

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class = CourseFilter


class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=SubjectFilter
    
class StaffViewSet(viewsets.ModelViewSet):
    queryset=Staff.objects.all()
    serializer_class=StaffSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=StaffFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_class=StudentFilter
