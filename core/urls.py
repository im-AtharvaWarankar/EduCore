from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (UniversityViewSet, CollegeViewSet, DepartmentViewset,CourseViewSet, SubjectViewSet,
      StaffViewSet, StudentViewSet)
    
router = DefaultRouter()
router.register(r'university', UniversityViewSet, basename='university')
router.register(r'college', CollegeViewSet, basename='college')
router.register(r'department', DepartmentViewset, basename='department')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'subject', SubjectViewSet, basename='subject')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
