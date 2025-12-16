
from django.db import models

class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class University(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    establishedYear = models.IntegerField()

    def __str__(self):
        return self.name
    
    
class College(BaseModel):
    
    name = models.CharField(max_length=100)
    universityId = models.ForeignKey(University, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Department(BaseModel):

    name = models.CharField(max_length=100)
    collegeId = models.ForeignKey(College, on_delete=models.CASCADE)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Course(BaseModel):
   
    title = models.CharField(max_length=100)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()

    def __str__(self):
        return self.title   

class Subject(BaseModel):
   
    name = models.CharField(max_length=100)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)  
    description = models.TextField()
   
    def __str__(self):
        return self.name

class Staff(BaseModel):
   
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE)
    subjectId= models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='subjects_taught')
    collegeId = models.ForeignKey(College, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Student(BaseModel):
   
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    enrollmentYear = models.IntegerField()
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"