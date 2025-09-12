from rest_framework import serializers
from core import models

class UniversitySerializer(serializers.ModelSerializer):
    university=serializers.SlugRelatedField(
        queryset=models.University.objects.all(),
        slug_field='name')
    class Meta:
        model = models.University
        fields = '__all__'

class CollegeSerializer(serializers.ModelSerializer):
    university=serializers.SlugRelatedField(
        queryset=models.University.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = models.College
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    college=serializers.SlugRelatedField(
        queryset=models.College.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = models.Department
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    department =serializers.SlugRelatedField(
        queryset=models.Department.objects.all(),
        slug_field="name"
    )
    class Meta:
        model = models.Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        queryset= models.Course.objects.all(),
        slug_field='title'
    )

    department = serializers.SlugRelatedField(
        queryset=models.Department.objects.all(),
        slug_field = 'name'
    )
    class Meta:
        model = models.Subject
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        queryset=models.Subject.objects.all(),
        slug_field='name'
    )
    department = serializers.SlugRelatedField(
        queryset=models.Department.objects.all(),
        slug_field= 'name'
    )
    class Meta:
        model = models.Staff
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        queryset=models.Course.objects.all(),
        slug_field='title')
    
    subject= serializers.SlugRelatedField(
        queryset=models.Subject.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = models.Student
        fields = '__all__'

