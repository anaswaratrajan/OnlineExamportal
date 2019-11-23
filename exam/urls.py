from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='base'),
    #path('', views.AddStudent, name='student_form'),
    path('student_form/', views.AddStudent.as_view(), name='student_form')
]
