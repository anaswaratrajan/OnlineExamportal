from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from exam.models import Student

class StudentForm(forms.ModelForm):


    class Meta:
        model = Student
        fields = ('register_no', 'student_name', 'student_email', 'student_marks')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Student'))
