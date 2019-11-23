from django.shortcuts import render
from django.views.generic import CreateView
from .models import Student
from .forms import StudentForm
from django.views.generic import UpdateView

# Create your views here.
from django.http import HttpResponse

class AddStudent(CreateView):
    model = Student
    fields = ('register_no', 'student_name', 'student_email', 'student_marks')
    success_url='/student_form'



class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'exam/student_form.html'
