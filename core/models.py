<<<<<<< HEAD

from django.db import models

class BaseModel(models.Model):
    id=models.AutoField(primary_key=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True

class University(BaseModel):
=======
from django.db import models


class University(models.Model):
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    establishedYear = models.IntegerField()

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
    
class College(BaseModel):
    
    name = models.CharField(max_length=100)
    universityId = models.ForeignKey(University, on_delete=models.CASCADE)
=======
class College(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
class Department(BaseModel):

    name = models.CharField(max_length=100)
    collegeId = models.ForeignKey(College, on_delete=models.CASCADE)
=======
class Department(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
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
=======
class Course(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.IntegerField()

    def __str__(self):
        return self.title

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  
    description = models.TextField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

<<<<<<< HEAD
class Student(BaseModel):
   
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    enrollmentYear = models.IntegerField()
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
=======
class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    enrollmentYear = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
>>>>>>> 37dac2585a83b08b1446e1c5dc0bcc315c31b66d

    def __str__(self):
        return f"{self.firstName} {self.lastName}"