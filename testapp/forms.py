from django import forms





class StudentForms(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    marks=forms.IntegerField()
    