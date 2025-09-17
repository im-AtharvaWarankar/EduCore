from rest_framework import serializers
from core import models

class UniversitySerializer(serializers.ModelSerializer):
    totalColleges = serializers.SerializerMethodField()
    class Meta:
        model = models.University
        fields = ['id','name','location','establishedYear','createdAt','updatedAt','totalColleges']

    def get_totalColleges(self,obj):
        colleges = models.College.objects.filter(universityId=obj)
        return CollegeSerializer(colleges,many=True).data
    
class CollegeSerializer(serializers.ModelSerializer):
    universityName = serializers.SerializerMethodField()
    universityLocation = serializers.SerializerMethodField()
    class Meta:
        model = models.College
        fields = ['id','name','universityId','location','createdAt','updatedAt','universityName','universityLocation']

    def get_universityName(self,obj):
        return obj.universityId.name
        
    def get_universityLocation(self,obj):
        return obj.universityId.location 

class DepartmentSerializer(serializers.ModelSerializer):
    coursesDept = serializers.SerializerMethodField()
    class Meta:
        model = models.Department
        fields = ['id','name','collegeId','hod','createdAt','coursesDept','updatedAt'
                  ]
    def get_coursesDept(self,obj):
        courses = models.Course.objects.filter(departmentId=obj)
        return CourseSerializer(courses,many=True).data

class CourseSerializer(serializers.ModelSerializer):
    courseSubjects=serializers.SerializerMethodField()
    courseDepartment=serializers.SerializerMethodField()
    class Meta:
        model = models.Course
        fields = [
            'id','title', 'departmentId','credits' ,'createdAt','updatedAt','courseSubjects','courseDepartment'
        ]
    def get_courseSubjects(self,obj):
        subjects = models.Subject.objects.filter(subjectId=obj)
        return CourseSerializer(subjects,many=True).data
    
    def get_courseDepartment(self,obj):
        return obj.departmentId.name


class SubjectSerializer(serializers.ModelSerializer):
    studentsEnrolled = serializers.SerializerMethodField()
    staffEnrolled = serializers.SerializerMethodField()
    class Meta:
        model = models.Subject
        fields = [
            'id', 'name', 'courseId', 'departmentId', 'description', 'createdAt', 'updatedAt', 'staffEnrolled', 'studentsEnrolled'
        ]
    def get_staffEnrolled(self, obj):
        staff = models.Staff.objects.filter(subjectId=obj)
        return [f"{s.firstName} {s.lastName}" for s in staff]
    def get_studentsEnrolled(self, obj):
        students = models.Student.objects.filter(subjectId=obj)
        return StudentSerializer(students, many=True).data

class StaffSerializer(serializers.ModelSerializer):
    staffCollege = serializers.SerializerMethodField()
    staffDepartment = serializers.SerializerMethodField()
    class Meta:
        model = models.Staff
        fields = [
           'id', 'firstName','lastName','departmentId','subjectId','position','createdAt','updatedAt','staffCollege','staffDepartment'
        ]
    def get_staffCollege(self,obj):
        return obj.collegeId.name
    
    def get_staffDepartment(self,obj):
        return obj.departmentId.name
class StudentSerializer(serializers.ModelSerializer):
    studentDepartment = serializers.SerializerMethodField()
    studentSubject = serializers.SerializerMethodField()
    studentCollege=serializers.SerializerMethodField()
    class Meta:
        model = models.Student
        fields = ['id','firstName','lastName','enrollmentYear','courseId','subjectId','studentDepartment','studentSubject','studentCollege','createdAt','updatedAt']

    def get_studentDepartment(self,obj):
        return obj.departmentId.name
    
    def get_studentSubject(self,obj):
        return obj.subjectId.name
    
    def get_studentCollege(self,obj):
        return obj.collegeId.name