from django.urls import path

from . import views

urlpatterns = [
    path('student_form/', views.AddStudent.as_view(), name='student_form')
]
