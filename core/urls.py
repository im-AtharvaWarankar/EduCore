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
