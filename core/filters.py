import django_filters
from core.models import University ,College,Department, Course, Subject, Staff ,Student

class UniversityFilter(django_filters.FilterSet):
    id =django_filters.UUIDFilter(lookup_expr='exact')
    name=django_filters.CharFilter(lookup_expr='icontains')
    establishedYear =django_filters.NumberFilter(lookup_expr='exact')
    establishedYear__gt=django_filters.NumberFilter(field_name='establishedYear', lookup_expr='gt')
    establishedYear__lt=django_filters.NumberFilter(field_name='establishedYear',lookup_expr='lt')
    location = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=University
        fields=['id','name','establishedYear','establishedYear__gt','establishedYear__lt','location']




class CollegeFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    name = django_filters.CharFilter(lookup_expr='icontains')
    location =django_filters.CharFilter(lookup_expr='icontains')

    universityId = django_filters.UUIDFilter(lookup_expr='exact')
    universityName=django_filters.CharFilter(field_name='universityId__name',lookup_expr='icontains')
    universityLocation=django_filters.CharFilter(field_name='universityId__location',lookup_expr='icontains')
    
    class Meta:
        model = College
        fields=[
            'id','name','location','universityId','universityName','universityLocation'
        ]

class DepartmentFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    name= django_filters.CharFilter(lookup_expr='icontains')
    hod = django_filters.CharFilter(lookup_expr='icontains')

    departmentCollegeName =django_filters.CharFilter(field_name='collegeId__name',lookup_expr='icontains')
    departmentUniversity=django_filters.CharFilter(field_name='collegeId__universityId__name',lookup_expr='icontains')
    departmentCollegeLocation=django_filters.CharFilter(field_name='collegeId__location',lookup_expr='icontains')

    class Meta:
        model =Department
        fields=[
            'id','name','hod','departmentCollegeName','departmentUniversity','departmentCollegeLocation'
        ]

class CourseFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(lookup_expr='exact')
    title=django_filters.CharFilter(lookup_expr='icontains')
    credits=django_filters.NumberFilter(lookup_expr='exact')

    courseDepartment = django_filters.CharFilter(field_name='departmentId__name',lookup_expr='icontains')
    courseCollege = django_filters.CharFilter(field_name='departmentId__collegeId__name',lookup_expr='icontains')

    class Meta:
        model = Course
        fields=[
            'id','title','credits','courseDepartment','courseCollege'
        ]

class SubjectFilter(django_filters.FilterSet):
        id = django_filters.NumberFilter(lookup_expr='exact')
        name = django_filters.CharFilter(lookup_expr='icontains')
        description = django_filters.CharFilter(lookup_expr='icontains')

        subjectDepartment= django_filters.CharFilter(field_name='courseId__departmentId__name',lookup_expr='icontains')
        subjectCourse=django_filters.CharFilter(field_name='courseId__name',lookup_expr='icontains')

        class Meta:
            model = Subject
            fields=[
                'id','name','subjectDepartment','subjectCourse'
            ]

class StaffFilter(django_filters.FilterSet):
        id = django_filters.NumberFilter(lookup_expr='exact')
        firstName = django_filters.CharFilter(lookup_expr='icontains')
        lastName=django_filters.CharFilter(lookup_expr='icontains')
        position=django_filters.CharFilter(lookup_expr='icontains')

        staffSubject=django_filters.CharFilter(field_name='subjectId__name',lookup_expr='icontains')
        staffCollege = django_filters.CharFilter(field_name='subjectId__courseId__departmentId__collegeId__name')

        class Meta:
            model = Staff
            fields =[
                'id','firstName','lastName','position','staffSubject','staffCollege'
            ]

class StudentFilter(django_filters.FilterSet):
        id=django_filters.NumberFilter(lookup_expr='exact')
        firstName = django_filters.CharFilter(lookup_expr='icontains')
        lastName = django_filters.CharFilter(lookup_expr='icontains')
        enrollmentYear = django_filters.NumberFilter(lookup_expr='exact')
        collegeId=django_filters.NumberFilter(lookup_expr='exact')

        studentStaff = django_filters.CharFilter(field_name='staffId__name',lookup_expr='icontains')
        studentCourse=django_filters.CharFilter(field_name='staffId__subjectId__courseId__name',lookup_expr='icontains')
        studentCollege=django_filters.CharFilter(field_name='staffId__subjectId__courseId__departmentId__collegeId__name')

        class Meta:
            model = Student
            fields=[
                 'id','firstName','lastName','enrollmentYear','studentStaff','studentCollege','studentCourse'
            ]
            