from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    establishedYear = models.IntegerField()

    def __str__(self):
        return self.name
    
class College(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
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
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    enrollmentYear = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"