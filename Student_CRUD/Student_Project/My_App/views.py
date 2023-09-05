from django.shortcuts import render, redirect
# Create your views here.
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def Insert_view(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Inserted Successfully")
            return redirect("/")
    # print(form)
    return render(request, "insert.html", {"form": form})


def show(request):
    students = Student.objects.all()
    return render(request, 'show.html', {"students": students})


def delete(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    messages.success(request,"Student Deleted Successfully")
    return redirect("/show")


def update(request, id):
    students = Student.objects.get(id=id)
    form = StudentForm(request.POST,instance=students)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Student Updated Successfully")
        return redirect("/show")

    return render(request,'update.html',{'students':students})