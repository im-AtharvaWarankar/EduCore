<<<<<<< HEAD
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
=======
from django.urls import path
from core.views import UniversityAPIView, CollegeAPIView, DepartmentAPIView, CourseAPIView, SubjectAPIView, StaffAPIView, StudentAPIView
urlpatterns = [
    path('University/', UniversityAPIView.as_view()),
    path('University/<str:name>/', UniversityAPIView.as_view()),
    path('College/', CollegeAPIView.as_view()),
    path('College/<str:name>/', CollegeAPIView.as_view()),   
    path('Department/', DepartmentAPIView.as_view()),
    path('Department/<str:name>/', DepartmentAPIView.as_view()),
    path('Course/', CourseAPIView.as_view()),
    path('Course/<str:title>/', CourseAPIView.as_view()),
    path('Subject/', SubjectAPIView.as_view()),
    path('Subject/<str:name>/', SubjectAPIView.as_view()),
    path('Staff/', StaffAPIView.as_view()),
    path('Staff/<str:firstName>/', StaffAPIView.as_view()),
    path('Student/', StudentAPIView.as_view()),
    path('Student/<str:firstName>/', StudentAPIView.as_view()),
 ]
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
