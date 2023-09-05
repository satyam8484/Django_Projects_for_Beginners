from django.shortcuts import render, redirect
# Create your views here.
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

def logout(request):
    auth.logout(request)
    return redirect("accounts/login")


def Insert_view(request):
    print(not request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("accounts/login")

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
    print(not request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("accounts/login")

    students = Student.objects.all()
    return render(request, 'show.html', {"students": students})


def delete(request, id):
    print(not request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("accounts/login")

    students = Student.objects.get(id=id)
    students.delete()
    messages.success(request,"Student Deleted Successfully")
    return redirect("/show")


def update(request, id):
    print(not request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect("/accounts/login")

    students = Student.objects.get(id=id)
    form = StudentForm(request.POST,instance=students)
    if form.is_valid():
        form.save(commit=True)
        messages.success(request, "Student Updated Successfully")
        return redirect("/show")

    return render(request,'update.html',{'students':students})