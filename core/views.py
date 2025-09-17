from rest_framework.views import APIView
from core.models import University, College, Department, Course, Subject, Staff, Student
from core.serializers import (UniversitySerializer,CollegeSerializer,DepartmentSerializer,CourseSerializer,SubjectSerializer,StaffSerializer,StudentSerializer)
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
<<<<<<< HEAD
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
=======

class UniversityAPIView(APIView):
    def get(self, request, name=None):
        if name:  
            try:
                university = University.objects.get(name=name) 
            except University.DoesNotExist:
                raise Http404 
            serializer = UniversitySerializer(university)  
            return Response(serializer.data)  
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            university = University.objects.get(pk=pk)
        except University.DoesNotExist:
            raise Http404
        serializer = UniversitySerializer(university, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            university = University.objects.get(pk=pk)
        except University.DoesNotExist:
            raise Http404
        university.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollegeAPIView(APIView):
    def get(self, request, name=None):
        if name:  
            try:
                college = College.objects.get(name=name)
            except College.DoesNotExist:
                raise Http404 
            serializer = CollegeSerializer(college)
            return Response(serializer.data)

        college = College.objects.all()
        serializer = CollegeSerializer(college, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            college = College.objects.get(pk=pk)
        except College.DoesNotExist:
            raise Http404
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            college = College.objects.get(pk=pk)
        except College.DoesNotExist:
            raise Http404
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentAPIView(APIView):
    def get(self, request, name=None):
        if name:
            try:
                department = Department.objects.get(name=name)
            except Department.DoesNotExist:
                raise Http404
            serializer = DepartmentSerializer(department)
            return Response(serializer.data)
        
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, name=None):
        if name:
            try:
                department = Department.objects.get(name=name)
            except Department.DoesNotExist:
                raise Http404
            department.delete()
            return Response({"message": f"Department '{name}' deleted successfully."})


class CourseAPIView(APIView):
    def get(self, request, title=None):
        if title:
            try:
                course = Course.objects.get(title=title)
            except Course.DoesNotExist:
                raise Http404
            serializer = CourseSerializer(course)
            return Response(serializer.data)
       
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    


    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, title=None):
        if title:
            try:
                course = Course.objects.get(title=title)
            except Course.DoesNotExist:
                raise Http404
            course.delete()
            return Response({"message": f"Course '{title}' deleted successfully."})
        
        return Response({"error": "Course name required to delete."}, status=400)


class SubjectAPIView(APIView):
    def get(self, request, name=None):
        if name:
            try:
                subject = Subject.objects.get(name=name)
            except Subject.DoesNotExist:
                raise Http404
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)
    
        

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StaffAPIView(APIView):
    def get(self, request, firstName=None):
       if firstName:
            try:
                staff = Staff.objects.get(firstName=firstName)
            except Staff.DoesNotExist:
                raise Http404
            serializer = StaffSerializer(staff)
            return Response(serializer.data)
       
       staff = Staff.objects.all()
       serializer = StaffSerializer(staff, many=True)
       return Response(serializer.data)

    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            staff = Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            staff = Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentAPIView(APIView):
    def get(self, request, firstName=None):
        if firstName:
            try:
                student = Student.objects.get(firstName=firstName)
            except Student.DoesNotExist:
                raise Http404
            serializer = StudentSerializer(student)
            return Response(serializer.data)
       
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
        
        

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404
        
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
