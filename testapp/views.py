from django.shortcuts import render

# Create your views here.



from testapp.forms import StudentForms
def student_form_view(request):
    submitted=False
    sname=''
    form=StudentForms()
    if request.method=='POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            print('Form Validation sucess')
            print('Name:',form.cleaned_data['name'])
            print('Roll No:',form.cleaned_data['rollno'])
            print('Marks:',form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True
    form=StudentForms()
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'sname':sname})