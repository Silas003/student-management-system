from django.db import models

class Student(models.Model):
    StudentID=models.PositiveIntegerField()
    StudentName=models.CharField(max_length=100)
    Email=models.EmailField()
    College=models.CharField(max_length=100)
    POS=models.CharField(max_length=100)
    YOA=models.DateField()

    def __str__(self) :
        return f'{self.StudentName}'
