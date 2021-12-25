import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from students.forms import StudentForm
from students.models import Student


def get_students(request):
    queryset = Student.objects.all()
    return render(request, 'students/index.html',
                  context={'students': queryset})


def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'GET':
        form = StudentForm(instance=student)

        return render(request, 'students/edit.html', context={'form': form})

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('students:list'))

        return render(request, 'students/edit.html', context={'form': form})

    return HttpResponse(status=405)


@require_http_methods(['GET', 'POST'])
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/edit.html')


@require_http_methods(['GET', 'POST'])
def create_students(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(5, 18),
            'phone': '+380967195593',
        }

        form = StudentForm(initial=data)

        return render(request, 'students/create.html',
                      context={'form': form})

    form = StudentForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('students:list'))

    return HttpResponse(str(form.errors), status=400)
