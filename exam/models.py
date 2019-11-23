from django.db import models

# Create your models here.

class Questions(models.Model):
    question_no = models.IntegerField()
    question_text = models.CharField(max_length=200)
    answer_choice_one = models.CharField(max_length=50)
    answer_choice_two = models.CharField(max_length=50)
    answer_choice_three = models.CharField(max_length=50)
    answer_choice_four = models.CharField(max_length=50)


    def __str__(self):
        number = str(self.question_no)
        return number

class Student(models.Model):
    register_no = models.IntegerField(default=1000)
    student_email = models.CharField(max_length=40)
    student_name = models.CharField(max_length=20)
    student_marks = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
