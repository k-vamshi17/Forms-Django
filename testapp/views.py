from django.shortcuts import render

# Create your views here.



from testapp.forms import StudentForms
def student_form_view(request):
    form=StudentForms()
    my_dict={'form':form}
    return render(request,'testapp/input.html',my_dict)
